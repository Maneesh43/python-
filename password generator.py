import secrets
import tkinter
from tkinter import Entry
from tkinter import filedialog
import os
from tkinter import Toplevel
from datetime import datetime
def time1():
    while(True):
           a=datetime.now().strftime("%I:%M:%S:%f:%p")
           l234.config(text=a,font="Helvetica 15 italic",fg="green")
           window.update()
def passgen():
    global passwor
    passwor=''
    cha="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM1234567890?"
    e1=Entry.get(e)
    e2=int(e1)
    for i in range(e2):
        passwor+=secrets.choice(cha)
    a2.config(text=passwor,font="Helvetica 22 italic",fg="green")
def savep():
    global e212
    top=Toplevel()
    top.geometry("200x200")
    top.title("Saving file")
    l21=tkinter.Label(top,text="Enter the name of file")
    l21.pack()
    e212=tkinter.Entry(top)
    e212.pack()
    b21=tkinter.Button(top,text="done",command=savep1,activeforeground="red",relief="groove")
    b21.pack()
    top.mainloop()
def savep1():
    e22=e212.get()
    f12=filedialog.askdirectory()
    os.chdir(f12)
    #i22=input("Enter the file name:")
    f1=open(e22,"w+")
    f1.write(passwor)
    f1.close()
    b23=tkinter.Button(text="quit",command=window.destroy)
    b23.pack()
     #f1=filedialog.asksaveasfilename(initialdir="/",title="select file",filetypes=(("text files","*txt"),("all files","*.*")))
window=tkinter.Tk()
window.title("Password Generator")
a=tkinter.Label(window,text="Password Generator",font="Helvetica 33 bold",fg="green")
a.pack()
a1=tkinter.Label(window,text="Enter the length of your password",font="Helvetica 15 italic",fg="red")
a1.pack()
e=tkinter.Entry()
e.focus()
e.pack()
b=tkinter.Button(window,command=passgen,text="generate",activebackground="green",relief="ridge")
b.pack()
b1=tkinter.Button(window,text="save",command=savep,activebackground="lightgreen",relief="groove")
b1.pack()
a2=tkinter.Label(text="")
a2.pack()
l234=tkinter.Label(window,text="")
l234.pack()
#time1()
window.mainloop()
