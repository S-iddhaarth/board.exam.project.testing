import moviepy.editor

"""this library is used here to write audio file from a video"""
from tkinter import *

"""Tkinter is  GuiProgramming toolkit for Python"""
from tkinter import filedialog

"""used in this program to get the path of the folder and files"""
import speech_recognition as sr

"""used to recognize audio and convert to text"""
from gtts import gTTS

import PyPDF2

root = Tk()

# VARIABLE SECTION

url = StringVar()
a = StringVar()
link1 = StringVar()
b = StringVar()
t = StringVar()
reader = StringVar()
clicked = StringVar()


def second_page():
    """this is basically the front page . it displays various button which take us to desired location . here the button defined are
    short_url which takes u to link shortner ,youtube_download- which takes u to a youtube video downloader ,vid_aud- takes you
     to audio extractor(extracts audio from video and give output in .wav codec) and aud_txt - recognises the audio and
      and make it to text and give output in .txt file"""
    short_url.grid(row=1, column=0)
    youtube_download.grid(row=2, column=0)
    vid_aud.grid(row=3, column=0)
    aud_txt.grid(row=4, column=0)


def pagedel():
    """this function basically clears all the buttons displayed from the second_page() function . this enables us to show
     the wigets like lables , buttons ,entry ,etc... which are invoked by clicking respective buttons on the same tab"""


    # If we want to unmap any widget from the screen or toplevel then forget() method is used. There
    # are two types of forget method forget_pack() ( similar to forget() ) and forget_grid() which are
    # used with pack() and grid() method respectively.

    short_url.grid_forget()
    youtube_download.grid_forget()
    vid_aud.grid_forget()
    aud_txt.grid_forget()



def tx():
    t = ent.get()
    output = gTTS(text=t, lang="en", slow=False)
    destination = filedialog.askdirectory()
    output.save(f"{destination}/output file.mp3")


def converter(variao):
    if variao == 'txt':
        root.filename_fo = filedialog.askopenfilename()
        with open(root.filename_fo, 'r') as file:
            file_content = file.read()
            output = gTTS(text=file_content, lang="en", slow=False)
            var = filedialog.askdirectory()
            output.save(var + "/output.mp3")

        if variao == 'pdf':
            root.filename_fo = filedialog.askopenfilename()
            reader = PyPDF2.PdfFileReader(root.filename_fo)
            page_stuff = reader.getPage(0)
            output = gTTS(text=page_stuff.extractText(), lang="en", slow=False)
            destination = filedialog.askdirectory()
            output.save(f"{destination}/output file.mp3")


def text_speech():

    pagedel()

    global lbl1
    global lbl2
    global lbl3
    global ent
    global drop
    global button1
    global button

    """this function gets the link of the youtube video that you want to download """
    # used in the command of youtube_download Button in the second_page() function

    root.configure(bg='#659DBD')

    lbl1 = Label(root, text='TEXT TO AUDIO', fg='white', bg='#659DBD', font=("Bold", 30))
    lbl2 = Label(root, text="(OR)", bg="#659DBD", fg='white', font=("Zapfino", 15))
    lbl3 = Label(root, text="PASTE YOUR TEXT", bg="#659DBD", fg='white', font=("Zapfino", 15))
    ent = Entry(root, width=50, bg='grey91')


    clicked.set('SELECT THE FILE TYPE')
    drop = OptionMenu(root, clicked, "txt", "pdf", "type")
    drop.config(bg='grey91', fg='#659DBD')

    lbl1.grid(row=0, column=0, padx=8, pady=21)
    button1 = Button(root, text="convert", command=tx)

    drop.grid()

    try:
        button = Button(root, text="convert", command=lambda: converter(clicked.get()))
        button.grid()
    except:
        print("error")

    lbl2.grid(pady=20)
    lbl3.grid()
    ent.grid()
    button1.grid()
    go_back = Button(text=">", command=yt_del())
    go_back.grid()


def yt_del():
    """this function will clear all the wigets in the screen which is present after calling  youtube_download() .
     it also also calls the second_page function so we return back to the initial page"""

    global t
    global lbl1
    global lbl2
    global lbl3
    global ent
    global drop
    global button1
    global button

    # unmap any widget from the screen or toplevel

    lbl1.grid_forget()
    lbl2.grid_forget()
    lbl3.grid_forget()
    ent.grid_forget()

    button1.grid_forget()
    button.grid_forget()

    second_page()


def vid_audioButton():
    """this function specifies the look of the tab once we click vid_audiobutton  """

    global vdotoaud
    global convert_button
    global vid_auidiobac
    global vid_aud
    pagedel()

    root.configure(bg='royal blue')


    # label section

    vdotoaud = Label(root, text="VIDEO TO AUDIO CONVERTER", font=('normal', 24), bg='royal blue', fg='black')
    vid_aud = Label(root,
                    text=' 79% OF CONSUMERS WOULD RATHER WATCH A VIDEO TO LEARN ABOUT\n A PRODUCT, THAN READ TEXT ON A PAGE.',
                    fg='peach puff', font=('bold', 12), bg='royal blue')

    # button section

    convert_button = Button(root, text="Browse...", bg='peach puff', fg='black', activebackground='paleTurquoise2',
                            width=10, height=2, font=('normal', 12), command=path_folder)
    vid_auidiobac = Button(root, text=">>", bg='peach puff', command=vid_aud_del)

    # The Grid geometry manager puts the widgets in a 2-dimensional table

    vdotoaud.grid(row=0, column=0, padx=74, pady=15)
    convert_button.grid(row=3, column=0)
    vid_aud.grid(row=4, column=0, pady=15)
    vid_auidiobac.grid(row=5, column=1)


def path_folder():
    """it gets the path of a video file and writes the audio file in .wav codec from a video """

    root.filename = filedialog.askopenfilename()
    video = moviepy.editor.VideoFileClip(root.filename)
    audio = video.audio
    audio.write_audiofile("audio.wav")


def vid_aud_del():
    """this function clears all the wigets which were invoked due to video_audiobutton() and
    calls the second_page() """

    global vdotoaud
    global convert_button
    global vid_auidiobac
    global vid_aud

    # unmap any widget from the screen or toplevel

    vdotoaud.grid_forget()
    convert_button.grid_forget()
    vid_auidiobac.grid_forget()
    vid_aud.grid_forget()

    second_page()

def audio_to_text():
    """it gets the name of the .txt file in which u want to store the text and specifies the look of the page """

    pagedel()
    root.configure(bg='light blue')

    global label_aud_txt
    global aud_txt_covbutton
    global aud_txt_back
    global aud_tex1
    global aud_tex2
    global name
    global Lable_name

    # entry section

    name = Entry(root, width=50, textvariable=b, bg="thistle1")

    # label section

    Lable_name = Label(root, text="enter the name of the text file in which you want to store the text ")
    aud_tex1 = Label(root, text='AUDIO TO TEXT', font=("Phosphate", 30), bg='light blue')
    aud_tex2 = Label(text='AUDIO RECORDING TECHNOLOGY WAS HIDDEN FROM REST OF THE WORLD FOR\n 15 YEARS BY NAZI REGIME',
                     font=('normal', 12), bg='light blue')
    label_aud_txt = Label(text="click the button below to convert", font=('normal', 26), bg='light blue')

    # button section

    aud_txt_covbutton = Button(text="browse...", font=("Herculanum",), activebackground='cornsilk2', command=text)
    aud_txt_back = Button(root, text=">>", command=aud_txt_del)

    # The Grid geometry manager puts the widgets in a 2-dimensional table

    name.grid(row=2, column=0, pady=5)
    Lable_name.grid(row=1, column=0)
    label_aud_txt.grid(row=3, column=0, padx=5)
    aud_txt_covbutton.grid(row=4, column=0, pady=20)
    aud_tex1.grid(row=0, column=0, padx=168, pady=25)
    aud_tex2.grid(row=5, column=0)
    aud_txt_back.grid(row=6, column=1)


def text():
    """get the path of the audio file and recognizes the audio and convert it to text and return in a .txt file"""

    global name

    AUD = filedialog.askopenfilename()
    r = sr.Recognizer()

    # with statement in Python is used in exception handling to make the code cleaner and much more readable.
    # It simplifies the management of common resources like file streams

    with sr.AudioFile(AUD) as source:
        audio = r.record(source)  # read the entire audio file
    print("converting..............")
    print(r.recognize_google(audio))
    file = open(b.get() + ".txt", 'w+')
    file.write(r.recognize_google(audio))
    file.close()


def aud_txt_del():
    """clears all the wigets which was invoked by the audio_to_text and calls back back second_page() function """

    global label_aud_txt
    global aud_txt_covbutton
    global aud_txt_back
    global aud_tex1
    global aud_tex2
    global name
    global Lable_name

    # unmap any widget from the screen or toplevel

    name.grid_forget()
    Lable_name.grid_forget()
    label_aud_txt.grid_forget()
    aud_txt_covbutton.grid_forget()
    aud_txt_back.grid_forget()
    aud_tex1.grid_forget()
    aud_tex2.grid_forget()
    second_page()


# all the buttons are defined below
# The Button widget is used to add buttons in a Python application. These buttons can display
# text or images that convey the purpose of the buttons. You can attach a function or a method
# to a button which is called automatically when you click the button
short_url = Button(root, text='SHORTEN YOUR URL', width=60, height=9, bg='paleTurquoise4',
                   activebackground='lavender')
youtube_download = Button(root, text='TEXTTO AUDIO', width=60, height=9, bg='paleTurquoise3',
                          activebackground='lavender', command=text_speech)
vid_aud = Button(root, text='VIDEO TO AUDIO', width=60, height=9, bg='paleTurquoise2', activebackground='lavender',
                 command=vid_audioButton)
aud_txt = Button(root, text='AUDIO TO TEXT', width=60, height=9, bg='paleTurquoise1', activebackground='lavender',
                 command=audio_to_text)
second_page()

# all the buttons are defined below
# The Button widget is used to add buttons in a Python application. These buttons can display
# text or images that convey the purpose of the buttons. You can attach a function or a method
# to a button which is called automatically when you click the button

root.mainloop()
