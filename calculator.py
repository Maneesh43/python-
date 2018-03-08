import tkinter
from tkinter import *
from tkinter import Entry
import time
def tick():
        try:
                while(True):
                        a=time.strftime('%I:%M:%S%p')
                        l.config(text=a,font="Helvetica 22 italic",fg="green")
                        window.update()
        except KeyboardInterrupt:
                l.config(text="Done with Exception")
                time.sleep(5)
def calculate():
	f=Entry.get(c)
	g=str(f)
	i=eval(g)
	h.config(text=i,font="Helvetica 22 italic",fg="green")
def clear():
	c.delete(0,END)
	h.config(text="")
def quit():
        window.destroy()
window=tkinter.Tk()
window.title("Calculator")
a=tkinter.Label(text="Calculator",font="Helvetica 33 bold",fg="Blue").pack()
b=tkinter.Label(text="Enter your expression in the Entry field").pack()
c=tkinter.Entry()
d=tkinter.Button(text="calculate",font="Times 15 bold",fg="green",command=calculate)
e=tkinter.Button(text="Clear",font="Times 15 bold",fg="green",command=clear)
b2=tkinter.Button(text="quit",command=quit,font="Times 15 bold",fg="red")
h=tkinter.Label(text="")
c.pack()
h.pack()
d.pack(padx=30,pady=20,side=LEFT)
e.pack(padx=80,pady=20,side=LEFT)
b2.pack(padx=120,pady=20,side=LEFT)
l1=tkinter.Label(text="")
l1.pack()
l=tkinter.Label(text="")
l.pack()
tick()
window.mainloop()
