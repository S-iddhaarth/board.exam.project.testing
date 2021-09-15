def short_del():
    '''this fucntion clears all the wigets present in the shortener_button() function and calls back second_page()  '''
    # this function is used in the command backwaybutton present in shorterner_button()
    global label_short
    global label_short2
    global entry_short
    global button_short
    global entry_short2
    global button_short2
    global backwaybutton

    # unmap any widget from the screen or toplevel

    label_short.grid_forget()
    label_short2.grid_forget()
    entry_short.grid_forget()
    button_short.grid_forget()
    entry_short2.grid_forget()
    button_short2.grid_forget()
    backwaybutton.grid_forget()
    second_page()


def shorterner_button():
    """it gets the link from user and displays the shortened  """
    # the shorterning process is done by other function called show() .
    # this function is used in the command of short_url button defined in the second_page() function
    pagedel()
    root.configure(bg='#12a4d9')
    global label_short
    global label_short2
    global entry_short
    global button_short
    global entry_short2
    global button_short2
    global backwaybutton
    # Lable section
    label_short = Label(root, text="ARE YOU TIRED OF USING LONG LINKS ?", font=("Phosphate", 35), fg="Black",
                        bg="#12a4d9")
    label_short2 = Label(root, text="DON'T WORRY WE HAVE A SOLUTION ""PASTE LINK BELOW TO SHOTEN", font=('Skia', 17),
                         bg="#12a4d9", fg="#d9138a")

    # entry section

    entry_short = Entry(root, width=50, bg='snow2')
    entry_short2 = Entry(root, bg='snow2')

    # buttons section

    button_short = Button(text='click here', fg="black", bg='#e2d810', font=('Helvetica', 9, 'bold'), height=2, width=9,
                          command=show)
    button_short2 = Button(root, text='COPY', font=('Helvetica', 10, 'bold'), height=2, width=7, fg='black',
                           bg='#e2d810', command=easycopy)
    backwaybutton = Button(root, text=">>", command=short_del)

    # The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split
    # into a number of rows and columns, and each “cell” in the resulting table can hold a widget

    label_short.grid(row=0, column=0, columnspan=2, pady=6)
    label_short2.grid(row=1, column=0, columnspan=2, pady=6)
    entry_short.grid(row=2, column=0, columnspan=2, pady=6)
    button_short.grid(row=3, column=0, columnspan=2, pady=6)
    entry_short2.grid(row=4, column=0, columnspan=2, pady=6)
    button_short2.grid(row=5, column=0, columnspan=2, pady=6)
    backwaybutton.grid(row=6, column=2)


def show():
    """shortens the url and return the shortened url"""

    short = a.get()  # gets the variable a
    linkS = pyshorteners.Shortener().tinyurl.short(short)  # shorten the url using a thirdparty "tinyurl"
    link1.set(linkS)


def easycopy():
    """THIS function copies  shortened url"""

    linkS = link1.get()
    pyperclip.copy(linkS)  # code to copy