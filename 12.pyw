from tkinter import *
import tkinter
import subprocess
import webbrowser
def select():
        global a
        a=tkinter.Entry(window)
        a.pack()
        b.pack()
def select1():
        ac=str(Entry.get(a))
        l=tkinter.Label(window,text="click here to ping")
        s=subprocess.Popen(['ping',ac],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        c=s.communicate()
        l.config(text=c,fg="green")
        l.pack()
def select2():
        s2=subprocess.Popen(['ipconfig'],stdout=subprocess.PIPE)
        c1=s2.communicate()
        l1=tkinter.Label(window,text="your ip config will be displayed below")
        l1.config(text=c1)
        l1.pack()
def about():
        lab=tkinter.Label(window,text="Under Development",fg="red")
        lab1=tkinter.Label(window,text="Done by Maneesh Thouti",fg="green")
        lab2=tkinter.Label(window,text="please provide your valuable suggestions")
        lab.pack()
        lab1.pack()
        lab2.pack()
def select3():
	webbrowser.open_new_tab("Techestate1.blogspot.com")
window=tkinter.Tk()
window.title("cmd gui")
menubar=Menu(window)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="ping",command=select)
filemenu.add_command(label="ipconfig",command=select2)
menubar.add_cascade(label="commands",menu=filemenu)
aboutmenu=Menu(menubar,tearoff=0)
aboutmenu.add_command(label="about",command=about)
aboutmenu.add_command(label="quit",command=window.quit)
aboutmenu.add_command(label="my blog",command=select3)
menubar.add_cascade(label="about",menu=aboutmenu)
b=tkinter.Button(window,text="ping",command=select1)
window.config(menu=menubar)
window.mainloop()
