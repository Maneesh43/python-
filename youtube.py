import tkinter
from tkinter import *
from tkinter import ttk
import time

import pafy
import os
def download():
    global url
    global video
    global streams
    url=Entry.get(e)
    video=pafy.new(url)
    streams=video.streams
    audiostreams=video.audiostreams
    i=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    for s in streams:
        a,b,c=(s.resolution,s.extension,s.get_filesize())
        d=str(c)
        listbox.insert(END,str(a),str(b))
        listbox.pack()
    l5=tkinter.Label(text="Enter the resolution no starting from 0")
    l5.pack()
    global e2
    e2=0
    e2=tkinter.Entry()
    e2.pack()
    b5=ttk.Button(text="ok",command=download1)
    b5.pack()
    download1()
def download1():
    e10=Entry.get(e2)
    e11=int(e10)
    a=streams[e11].download(quiet=False,filepath='c:\\users\\maneesh\\desktop')
    print(a)
window=tkinter.Tk()
scrollbar=ttk.Scrollbar()
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(window,yscrollcommand=scrollbar.set)
window.title("Youtube downloader")
window.geometry("900x900")
l=tkinter.Label(text="Youtube Downloader",font="Helvetica 33 bold",fg="blue")
l.pack()
l1=tkinter.Label(text="Enter the url",font="Times 11 italic",fg="green")
l1.pack()
e=tkinter.Entry(window)
e.pack(ipadx=5,ipady=5)
b=ttk.Button(text="Download",command=download,font="Helvetica 22 italic",fg="green")
b.pack()
l2=tkinter.Label(text="")
l2.pack()
l11=tkinter.Label(text="")
l11.pack()
scrollbar.config(command=listbox.yview)
window.mainloop()
