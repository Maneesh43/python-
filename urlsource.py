
import tkinter
import tkinter.scrolledtext as tstk
from tkinter import ttk,Entry,LEFT,END
from bs4 import BeautifulSoup
import urllib.request as u
def gog(_event=None):
    #a=str(input("Enter the URL"))
    a=Entry.get(e1)
    b="http://"+a
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
window=tkinter.Tk()
window.title("Get Source code of web pages")
l=tkinter.Label(text="Enter  the URL",font="Helvetica 15 italic",fg="green")
ed=tstk.ScrolledText(font="Helvetica 15 italic",fg="blue")
e1=tkinter.Entry()
e1.focus()
l.pack()
e1.pack(padx=10,pady=10)
b1=ttk.Button(text="Get",command=gog)
#b1.bind('<Return>',gog)
b2=ttk.Button(text="clear",command=gog1)
#b2.bind('<Return>',gog1)
b1.pack(padx=10,side=LEFT,pady=10)
b2.pack(padx=25,side=LEFT,pady=10)
ed.pack()
window.mainloop()

