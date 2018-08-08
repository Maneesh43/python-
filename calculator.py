import tkinter,threading
from tkinter import Entry,Button,StringVar,GROOVE,LEFT,END
import time
def tick():
             a=time.strftime('%I:%M:%S %p')
             l.config(text=a,font="Helvetica 22 italic",fg="green")
             window.after(1,tick)
             window.update_idletasks()
def calculate():
	f=Entry.get(c)
	g=str(f)
	i=eval(g)
	h.config(text=i,font="Helvetica 33 italic",fg="green")
def clear():
	c.delete(0,END)
	h.config(text="")
def quit():
        window.destroy()
def tracer(a,b,c):
        calculate()
window=tkinter.Tk()
var=StringVar()
var.trace('w',tracer)
window.title("Calculator")
a=tkinter.Label(text="Calculator",font="Helvetica 33 bold",fg="Blue").pack()
b=tkinter.Label(text="Enter your expression in the Entry field").pack()
c=tkinter.Entry(textvariable=var)
d=tkinter.Button(text="calculate",font="Helvetica 15 italic",fg="green",command=calculate,relief=GROOVE,highlightcolor="green")
e=tkinter.Button(text="Clear",font="Helvetica 15 bold",fg="green",command=clear,relief=GROOVE)
e.focus()
b2=tkinter.Button(text="quit",command=quit,font="Helvetica 15 bold",fg="red",relief=GROOVE)
h=tkinter.Label(text="")
c.pack(ipady=5)
h.pack()
d.pack(padx=40,pady=20,side=LEFT)
e.pack(padx=80,pady=20,side=LEFT)
b2.pack(padx=120,pady=20,side=LEFT)
l1=tkinter.Label(text="")
l1.pack()
l=tkinter.Label(text="")
l.pack()
t1=threading.Thread(target=tick)
t1.start()
#tick()
window.mainloop()


