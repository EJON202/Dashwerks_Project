from tkinter import *
    master = Tk()

    def change_text():
        my_var.set("Second click")

    my_var = StringVar()
    my_var.set("First click")
    label = Label(mas,textvariable=my_var,fg="red")
    button = Button(mas,text="Submit",command = change_text)
    button.pack()
    label.pack()

    master.mainloop()
    
