#  This script builds on v002 and creates text boxes on each of the current rectangles (that will later be bar graphs


from tkinter import*
root = Tk()
root.geometry("800x480") #makes main window
#my_canvas = Canvas(root, width=800, height=480, bg="black") #background



def canvasRectangles():
	# my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
	# Rectangle x1, y1: Top Left
	# Rectange x2, y2: bottom Right
	my_canvas.create_rectangle(30, 30, 350, 200, fill="pink")  #4 corner graphs
	my_canvas.create_rectangle(30, 280, 350, 440, fill="blue")
	my_canvas.create_rectangle(450, 30, 770, 200, fill="red")
	my_canvas.create_rectangle(450, 280, 770, 440, fill="green")
	my_canvas.pack()	#related to graphs

def writeBarGraphText():
	Label(root, text="System Test1", bg="black", fg="white",font=("Arial", 20)).place(x=100, y=80)  #text
	Label(root, text="System Test2", bg="black", fg="white",font=("Arial", 20)).place(x=550, y=80)
	Label(root, text="System Test3", bg="black", fg="white",font=("Arial", 20)).place(x=160, y=360)
	Label(root, text="System Test4", bg="black", fg="white",font=("Arial", 20)).place(x=640, y=360)

writeBarGraphText()
canvasRectangles()

root.mainloop()
