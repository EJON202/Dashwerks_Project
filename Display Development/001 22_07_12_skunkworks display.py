#22_07_12_save1.py

#  This script is to create a GUI into the 7in display for demonstration purposes


from tkinter import*

root = Tk()
root.geometry("800x480") #makes main window

my_canvas = Canvas(root, width=800, height=480, bg="black") #first rectangle

my_canvas.create_rectangle(50, 50, 350, 200, fill="pink")
my_canvas.create_rectangle(50, 250, 750, 200, fill="blue")

my_canvas.pack()

#create_line = (x1, y1, x2, y2, fill="color")

# my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
# Rectangle x1, y1: Top Left
# Rectange x2, y2: bottom Right

root.mainloop()
