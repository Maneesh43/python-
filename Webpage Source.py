import os
os.system('pip install validators')
import threading,validators
import tkinter
import tkinter.scrolledtext as tstk
from tkinter import ttk,Entry,LEFT,END,messagebox,StringVar
from bs4 import BeautifulSoup
import urllib.request as u
def gog(_event=None):
    global b
    #a=str(input("Enter the URL"))
    a=Entry.get(e1)
    b="http://"+a
    if(validators.url(b)==True and  "www" and "com" in b):pass
    else:messagebox.showinfo("enter valid url","Please enter valid url") and e1.focus()
    c=u.urlopen(b)
    d=c.read()
    #print(d)
    e=BeautifulSoup(d)
    f=e.prettify()
    #print(f)
    ed.insert('insert',f)
def gog1():
    e1.delete(0,END)
    ed.delete('1.0',END)
    e1.focus()
def gog2():
    t1=threading.Thread(target=gog,args=[])
    t1.start()
#def tracer(a,b,c):
    #gog2()
window=tkinter.Tk()
window.title("Get Source code of web pages")
var=StringVar()
#var.trace('w',tracer)
l=tkinter.Label(text="Enter  the URL",font="Helvetica 15 italic",fg="green")
ed=tstk.ScrolledText(font="Helvetica 15 italic",fg="blue")
e1=tkinter.Entry(fg="red",font="Helvetica 12 italic",cursor="pencil")
e1.focus()
e1.bind('<Return>',gog)
l.pack()
e1.pack(padx=10,pady=10,expand=True)
b1=ttk.Button(text="Get",command=gog2)
#b1.focus_set()
b1.bind('<Return>',gog)
b2=ttk.Button(text="clear",command=gog1)
b2.bind('<Delete>',gog1)
b1.pack(padx=10,side=LEFT,pady=10)
b2.pack(padx=25,side=LEFT,pady=10)
ed.pack()
window.mainloop()

