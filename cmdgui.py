from tkinter import *
from time import strftime
import tkinter
import subprocess
import os
from tkinter import messagebox
from tkinter import ttk
import tkinter.scrolledtext as tstk
def select():
        global a
        a=tkinter.Entry(frame)
        b=ttk.Button(frame,command=select1,text="ping")    
        a.pack()
        b.pack()
        edit_t.pack(fill="both")
def select1():
        ac=str(Entry.get(a))
        s=subprocess.Popen(['ping',ac],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        c=s.communicate()
        edit_t.insert('insert',c)
def select2():
        s2=subprocess.Popen(['ipconfig'],stdout=subprocess.PIPE)
        c1=s2.communicate()
        l1=tkinter.Label(window,text="your ip config will be displayed below")
        l1.config(text=c1)
        l1.pack()
def about():
    messagebox.showinfo(message="Done By Maneesh")
def select3():
	os.system("start""http:\\Techestate1.blogspot.com")
def select4():
        l=tkinter.Label(window,text="would you like to create a new hotspot or continue with exixting one")
        l.pack()
        b=ttk.Button(window,text="create",command=hotspotc)
        b.pack()
        l1=tkinter.Label(window,text="click this if you have already created a hotspot profile")
        l1.pack()
        b1=ttk.Button(window,text="start hotspot",command=hotstar)
        b1.pack()
        l2=ttk.Button(window,text="stop hotspot",command=hotstop)
        l2.pack()
def hotspotc():
        l=tkinter.Label(window,text="enter ssid for your hotspot")
        l.pack()
        global en,en1
        en=tkinter.Entry(window)
        en.pack()
        l1=tkinter.Label(window,text="Enter password(between 8 to 63 characters) for your hotspot")
        l1.pack()
        en1=tkinter.Entry(window)
        en1.pack()
        b11=ttk.Button(window,text="click here",command=start)
        b11.pack()
def start():
        a=Entry.get(en)
        b=Entry.get(en1)
        a=subprocess.Popen(['netsh','wlan','set','hostednetwork','mode=allow','ssid=',a,'key=',b,'keyusage=persistent'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        co=a.communicate()
        b1=a.returncode
        if(b1==1):print("succeded in creating hotspot\n",co)
        else:print("failed to create the hotspot\n",co)
def hotstar():
        a=subprocess.Popen(['netsh','wlan','start','hostednetwork'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        b=a.communicate()
        print(b)
def hotstop():
        a=subprocess.Popen(['netsh','wlan','stop','hostednetwork'])
        print(a)
def select7():
        b1=ttk.Button(window,text="shutdown",command=select8).pack()
        b2=ttk.Button(window,text="restart",command=select9).pack()
        b3=ttk.Button(window,text="logoff",command=select10).pack()
        b4=ttk.Button(window,text="remote shutdown",command=select11).pack()
        b5=ttk.Button(window,text="abort shutdown",command=select12).pack()
        b6=ttk.Button(window,text="immediate shutdown",command=select13).pack()
        b7=ttk.Button(window,text="Hibernate",command=select14).pack()
def select8():
        s=subprocess.Popen(['shutdown/s'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
def select9():
        s=subprocess.Popen(['shutdown/r'],shell=True,shstdin=subprocess.PIPE,stdout=subprocess.PIPE)
def select10():
        s=subprocess.Popen(['shutdown/l'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
def select11():
        s=subprocess.Popen(['shutdown/i'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
def select12():
        s=subprocess.Popen(['shutdown/a'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
def select13():
        s=subprocess.Popen(['shutdown/p'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
def select14():
         s=subprocess.Popen(['shutdown/h'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
def selectt():
        la=tkinter.Label()
        t=strftime("%b %d %Y %H:%M:%S")
        print(t)
window=tkinter.Tk()
frame=tkinter.Frame(window)
frame.pack()
edit_t=tstk.ScrolledText(font="Helvetica 15 italic",fg="green")
window.title("cmd gui")
window.geometry("700x500")
menubar=Menu(window)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="ping",command=select)
filemenu.add_command(label="ipconfig",command=select2)
filemenu.add_command(label="Hotspot",command=select4)
filemenu.add_command(label="shutdown",command=select7)
menubar.add_cascade(label="commands",menu=filemenu)
aboutmenu=Menu(menubar,tearoff=0)
aboutmenu.add_command(label="about",command=about)
aboutmenu.add_command(label="quit",command=lambda:window.destroy())
aboutmenu.add_command(label="my blog",command=select3)
filemenu.add_command(label="Time",command=selectt)
menubar.add_cascade(label="about",menu=aboutmenu)
window.config(menu=menubar)
window.mainloop()
