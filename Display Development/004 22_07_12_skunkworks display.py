#  This script builds on v002 and creates text boxes on each of the current rectangles (that will later be bar graphs)


from tkinter import*
root = Tk()
my_canvas = Canvas(root, width=800, height=480, bg="black") #makes main window


def canvasRectangles():
	# my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink", outline='color', width='number of pixles')
	# Rectangle x1, y1: Top Left
	# Rectange x2, y2: bottom Right
	my_canvas.create_rectangle(30, 30, 350, 200, fill="pink", outline="white", width=5)  #4 corner graphs
	my_canvas.create_rectangle(30, 280, 350, 440, fill="blue", outline="white", width=5)
	my_canvas.create_rectangle(450, 30, 770, 200, fill="red", outline="white", width=5)
	my_canvas.create_rectangle(450, 280, 770, 440, fill="green", outline="white", width=5)
	my_canvas.pack()	#related to graphs

def writeBarGraphText():
	Label(root, text="Oil Pressure", bg="black", fg="white",font=("Arial", 20)).place(x=100, y=90)  #text
	Label(root, text="Water Temperature", bg="black", fg="white",font=("Arial", 20)).place(x=500, y=90)
	Label(root, text="Pyrometer", bg="black", fg="white",font=("Arial", 20)).place(x=100, y=340)
	Label(root, text="Fuel Pressure", bg="black", fg="white",font=("Arial", 20)).place(x=530, y=340)

writeBarGraphText()
canvasRectangles()



root.mainloop()
