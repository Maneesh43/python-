import tkinter,pyautogui,time,psutil
def pos1():
    x4=psutil.cpu_percent(interval=0.1)
    x5=psutil.virtual_memory()
    x8=psutil.sensors_battery()
    x9=x8[0]
    x10=x8[1]
    x12=x10/60
    x11=x8[2]
    x6=x5[1]
    x7=x6/(1024*1024)
    x1=time.strftime("%a %b %Y")
    x2=time.strftime("%Z")
    x3=time.strftime("%r")
    x=pyautogui.position()
    y.config(text=x,font="Helvetica 16 italic",fg="green")
    y1.config(text=x1,font="Helvetica 16 bold",fg="blue")
    y2.config(text=x2,font="Helvetica 16 bold",fg="blue")
    y3.config(text=x3,font="Helvetica 16 bold",fg="blue")
    y4.config(text="CPU Usage :%d"%x4+"/100",font="Helvetica 16 bold",fg="blue")
    y5.config(text="Available Ram:%d"%x7+"Mb",font="Helvetica 16 bold",fg="blue")
    y6.config(text="charge percent:%d"%x9+"/100",font="Helvetica 16 bold",fg="blue")
    y7.config(text="Minutes left to charge completely:%d"%x12,font="Helvetica 16 bold",fg="blue")
    y8.config(text="Power Connected:%s"%x11,font="Helvetica 16 italic",fg="blue")
    window.update()
    window.after(1,pos1)
window=tkinter.Tk()
y=tkinter.Label(text="")
y1=tkinter.Label(text="")
y2=tkinter.Label(text="")
y3=tkinter.Label(text="")
y4=tkinter.Label(text="")
y5=tkinter.Label(text="")
y6=tkinter.Label(text="")
y7=tkinter.Label(text="")
y8=tkinter.Label(text="")
y.pack()
y1.pack()
y2.pack()
y3.pack()
y4.pack()
y5.pack()
y6.pack()
y7.pack()
y8.pack()
pos1()
window.mainloop()

            
