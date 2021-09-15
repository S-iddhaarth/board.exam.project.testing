from tkinter import *
root = Tk()
def show():
    a = Label(root,text = var.get())
    a.pack()
var = StringVar()
drop = OptionMenu(root,var,"y","r","u","not","working")
drop.pack()
button =Button(root,text ="click", command = show)
button.pack()
root.mainloop()