import tkinter
from tkinter import *
from tkinter import Entry
import time
def calculate():
	f=Entry.get(c)
	g=str(f)
	i=eval(g)
	h.config(text=i,font="Helvetica 22 italic",fg="green")
	window.update_idletasks()
def clear():
	c.delete(0,END)
	h.config(text="")
window=tkinter.Tk()
window.title("Calculator")
a=tkinter.Label(text="Calculator",font="Helvetica 33 bold",fg="Blue").pack()
b=tkinter.Label(text="Enter your expression in the Entry field").pack()
c=tkinter.Entry()
d=tkinter.Button(text="calculate",font="Times 15 bold",fg="green",command=calculate)
e=tkinter.Button(text="Clear",font="Times 15 bold",fg="green",command=clear)
h=tkinter.Label(text="")
c.pack()
h.pack()
d.pack(padx=30,pady=20,side=LEFT)
e.pack(padx=80,pady=20,side=LEFT)
window.mainloop()


