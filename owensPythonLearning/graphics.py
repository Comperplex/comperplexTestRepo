import tkinter
import time

top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg='black', height=250, width=250)
rectangle = canvas.create_rectangle(0, 0, 50, 50, fill='white')
canvas.pack()

def animation():
	for i in range(100):
		canvas.move(rectangle, 1, 0)
		canvas.update()
		time.sleep(0.025)

top.after(0, animation())
top.mainloop()
