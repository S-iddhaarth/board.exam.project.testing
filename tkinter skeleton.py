from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import PyPDF2
root = Tk()

langu = StringVar()
reader = StringVar()


def converter (variao):
    if variao == 'txt':
        root.filename_fo = filedialog.askopenfilename()
        with open(root.filename_fo ,'r') as file:
            file_content = file.read()
            output = gTTS(text=file_content, lang="en", slow=False)
            var = filedialog.askdirectory()
            output.save(var + "/output.mp3")

    if variao == 'pdf':
         root.filename_fo = filedialog.askopenfilename()
         reader = PyPDF2.PdfFileReader(root.filename_fo)
         page_stuff = reader.getPage(0)
         output = gTTS(text=page_stuff.extractText(), lang= "en", slow=False)
         destination = filedialog.askdirectory()
         output.save(f"{destination}/output file")



clicked = StringVar()
drop = OptionMenu(root,clicked ,"txt","pdf","type")


drop.pack()
try :
    button = Button(root,text="convert", command = lambda : converter(clicked.get()))
    button.pack()
except:
    print("error")

root.mainloop()