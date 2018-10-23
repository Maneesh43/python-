import tkinter as tk
from tkinter import ttk
import wmi
def brightt():
   a=wmi.WMI(namespace='wmi')
   sc = s.get()
   c=a.WmiMonitorBrightnessMethods()[0]
   c.WmiSetBrightness(sc,0)
def tracer(t1,t2,t3):
    brightt()
global s
r=tk.Tk()
s=tk.IntVar()
s.set('30')
ttk.Scale(from_=0,to_=100,variable=s,command=brightt()).pack()
aa=tk.Entry(textvariable=s,fg="green")
s.trace('w',tracer)
aa.delete(0,'end')
aa.focus()
aa.pack()
#tk.Label(textvariable=s).pack()
r.mainloop()
