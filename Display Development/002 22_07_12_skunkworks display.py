#22_07_12_save1.py

#  This script creates a GUI with four boxes. These will later be bar graphs. This is v002.


from tkinter import*

root = Tk()
root.geometry("800x480") #makes main window

my_canvas = Canvas(root, width=800, height=480, bg="black") #background

# my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
# Rectangle x1, y1: Top Left
# Rectange x2, y2: bottom Right

my_canvas.create_rectangle(30, 30, 350, 200, fill="pink")  #4 corner graphs
my_canvas.create_rectangle(30, 280, 350, 440, fill="blue")
my_canvas.create_rectangle(450, 30, 770, 200, fill="red")
my_canvas.create_rectangle(450, 280, 770, 440, fill="green")
my_canvas.pack()	#related to graphs



root.mainloop()
