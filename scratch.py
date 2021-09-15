import moviepy.editor

"""this library is used here to write audio file from a video"""
from tkinter import Label, Button, Entry, Tk, mainloop, StringVar, OptionMenu, filedialog

"""Tkinter is  GuiProgramming toolkit for Python"""

import speech_recognition as sr

"""used to recognize audio and convert to text"""
from gtts import gTTS

import PyPDF2

# FUNCTION SECTION

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""FUNCTION RELATED TO FIRST PAGE"""


######################################################################################################################
def first_page():
    """this is basically the front page . it displays various button which take us to desired location . here the button defined are
    text to audio which takes u to text to audio converter ,video to audio takes you to video to audio converter,audio to text which
    takes you to audio to text converter"""

    youtube_download.grid(row=2, column=0)
    vid_aud.grid(row=3, column=0)
    aud_txt.grid(row=4, column=0)


def page_del():
    """removes the content of first page"""

    youtube_download.grid_forget()
    vid_aud.grid_forget()
    aud_txt.grid_forget()


####################################################################################################################


"""FUNCTIONS RELATED TO CONVERTING TEXT TO AUDIO"""


####################################################################################################################
def text_speech():
    """displays the labels , button and entry related to converting text to audio """

    page_del()
    root.configure(bg='#659DBD')
    lbl1.grid(row=0, column=0, padx=8, pady=21)
    drop.grid()
    button.grid()
    lbl2.grid(pady=20)
    lbl3.grid()
    ent.grid()
    button1.grid()
    go_back.grid()


def tx():
    """converts user typed or copy pasted text into output.mp3 file and store it wherever you want"""

    t = ent.get()
    output = gTTS(text=t, lang="en", slow=False)
    destination = filedialog.askdirectory()
    output.save(f"{destination}/output file.wav")


def converter(variao):
    """converts the text file and pdf file to output.mp3 and stores it wherever you want"""

    if variao == 'txt':
        root.filename_fo = filedialog.askopenfilename()

        with open(root.filename_fo, 'r') as file:
            file_content = file.read()
            output = gTTS(text=file_content, lang="en", slow=False)
            var = filedialog.askdirectory()
            output.save(var + "/output.wav")

    if variao == 'pdf':
        root.filename_fo = filedialog.askopenfilename()
        reader = PyPDF2.PdfFileReader(root.filename_fo)
        page_stuff = reader.getPage(0)
        output = gTTS(text=page_stuff.extractText(), lang="en", slow=False)
        destination = filedialog.askdirectory()
        output.save(f"{destination}/output file.mp3")


def text_speech_del():
    """removes the content created by text_speech() function"""

    go_back.grid_forget()
    lbl1.grid_forget()
    lbl2.grid_forget()
    lbl3.grid_forget()
    ent.grid_forget()
    drop.grid_forget()
    button1.grid_forget()
    button.grid_forget()

    first_page()


####################################################################################################################


"""FUNCTION RELATED TO CONVERTING VIDEO TO AUDIO """


####################################################################################################################
def vid_audioButton():
    """displays the labels , buttons and entry related to converting video to audio"""

    page_del()
    vdotoaud.grid(row=0, column=0, padx=74, pady=15)
    convert_button.grid(row=3, column=0)
    vid_lable.grid(row=4, column=0, pady=15)
    vid_auidiobac.grid(row=5, column=1)


def path_folder():
    """it gets the path of a video file and writes the audio file in .wav codec from a video """

    root.filename = filedialog.askopenfilename()
    video = moviepy.editor.VideoFileClip(root.filename)
    audio = video.audio
    audio.write_audiofile("audio.wav")


def vid_aud_del():
    """this function clears all the wigets which were invoked due to video_audiobutton() and
    calls the first_page() """

    # unmap any widget from the screen or toplevel

    vdotoaud.grid_forget()
    convert_button.grid_forget()
    vid_auidiobac.grid_forget()
    vid_lable.grid_forget()

    first_page()


####################################################################################################################

"""functions related to converting audio to text"""


####################################################################################################################

def audio_to_text():
    pass


####################################################################################################################

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
root = Tk()

clicked = StringVar()

# BUTTONS RELATED TO FIRST PAGE
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

youtube_download = Button(root, text='TEXTTO AUDIO', width=60, height=9, bg='paleTurquoise3',
                          activebackground='lavender', command=text_speech)

vid_aud = Button(root, text='VIDEO TO AUDIO', width=60, height=9, bg='paleTurquoise2', activebackground='lavender',
                 command=vid_audioButton)

aud_txt = Button(root, text='AUDIO TO TEXT', width=60, height=9, bg='paleTurquoise1', activebackground='lavender',
                 command=audio_to_text)

first_page()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""BUTTONS,LABELS AND ENTRY RELATED TO TEXT TO SPEECH CONVERTER"""

####################################################################################################################

"""LABELS"""

lbl1 = Label(root, text='TEXT TO AUDIO', fg='white', bg='#659DBD', font=("Bold", 30))
lbl2 = Label(root, text="(OR)", bg="#659DBD", fg='white', font=("Zapfino", 15))
lbl3 = Label(root, text="PASTE YOUR TEXT", bg="#659DBD", fg='white', font=("Zapfino", 15))

"""ENTRY"""

ent = Entry(root, width=50, bg='grey91')

"""DROP DOWN BOX """

clicked.set('SELECT THE FILE TYPE')
drop = OptionMenu(root, clicked, "txt", "pdf")
drop.config(bg='grey91', fg='#659DBD')

"""BUTTONS"""

button = Button(root, text="convert", command=lambda: converter(clicked.get()))
button1 = Button(root, text="convert", command=tx)
go_back = Button(root, text=">", command=text_speech_del)

####################################################################################################################

# labels and buttons related to video to audio converter

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# label section

vdotoaud = Label(root, text="VIDEO TO AUDIO CONVERTER", font=('normal', 24), bg='royal blue', fg='black')
vid_lable = Label(root,
                  text=' 79% OF CONSUMERS WOULD RATHER WATCH A VIDEO TO LEARN ABOUT\n A PRODUCT, THAN READ TEXT ON A PAGE.',
                  fg='peach puff', font=('bold', 12), bg='royal blue')

# button section

convert_button = Button(root, text="Browse...", bg='peach puff', fg='black', activebackground='paleTurquoise2',
                        width=10, height=2, font=('normal', 12), command=path_folder)
vid_auidiobac = Button(root, text=">>", bg='peach puff', command=vid_aud_del)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
root.mainloop()