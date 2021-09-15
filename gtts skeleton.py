from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import PyPDF2
root = Tk()
root.configure(bg='#659DBD')


reader = StringVar()
t = StringVar

lbl1 = Label(root, text='TEXT TO AUDIO', fg='white', bg='#659DBD', font=("Bold", 30))
lbl2 = Label(root, text="(OR)", bg="#659DBD",fg='white', font=("Zapfino", 15))
lbl3 = Label(root, text="PASTE YOUR TEXT", bg="#659DBD",fg='white', font=("Zapfino", 15))
ent=Entry(root,width=50,bg='grey91')
def tx():
    t =ent.get()
    output = gTTS(text=t, lang= "en", slow=False)
    destination = filedialog.askdirectory()
    output.save(f"{destination}/output file.mp3")
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
         output.save(f"{destination}/output file.mp3")



clicked = StringVar()
clicked.set('SELECT THE FILE TYPE')
drop = OptionMenu(root,clicked ,"txt","pdf","type")
drop.config(bg='grey91',fg='#659DBD')

lbl1.grid(row = 0 ,column =0,padx=8,pady=21)
button1 = Button(root,text="convert", command = tx )



drop.grid()

try :
    button = Button(root,text="convert", command = lambda : converter(clicked.get()))
    button.grid()
except:
    print("error")


lbl2.grid(pady=20)
lbl3.grid()
ent.grid()
button1.grid()

root.mainloop()

