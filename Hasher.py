import tkinter,threading,os
import hashlib as h
from tkinter import ttk,filedialog
def md5f():
    md5 = h.md5()
    print(fil)
    with open(fil, buffering=0,mode="rb") as ak:
        while True:
            d = ak.read(65536 )
            if not d:
                break
            md5.update(d)
            l3.config(text="Md5 hash is"+" "+md5.hexdigest(),font="Helvetica 12 italic",fg="green")
def sha224f():
    sha224=h.sha224()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sha224.update(d)
            l3.config(text="sha224 hash is" + " " +sha224.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha1f():
    sha1=h.sha1()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sha1.update(d)
            l3.config(text="sha1 hash is" + " " + sha1.hexdigest(), font="Helvetica 12 italic", fg="green")
def blake2bf():
    bl=h.blake2b()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            bl.update(d)
            l3.config(text="blake2b hash is" + " " + bl.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha384f():
    sh=h.sha384()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh.update(d)
            l3.config(text="sha384 hash is" + " " + sh.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha3512f():
    sh35=h.sha3_512()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh35.update(d)
            l3.config(text="sh3_512 hash is" + " " + sh35.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha3256f():
    sh325=h.sha3_256()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh325.update(d)
            l3.config(text="sha3_256 hash is" + " " + sh325.hexdigest(), font="Helvetica 12 italic", fg="green")
def shake256f():
    sh12=h.shake_256()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh12.update(d)
            l3.config(text="shake_256 hash is" + " " + sh12.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha3224f():
    sh322=h.sha3_224()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh322.update(d)
            l3.config(text="sha3_224 hash is" + " " + sh322.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha512f():
    sh51=h.sha512()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh51.update(d)
            l3.config(text="sha512 hash is" + " " + sh51.hexdigest(), font="Helvetica 12 italic", fg="green")
def blake2sf():
    bl2=h.blake2s()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            bl2.update(d)
            l3.config(text="blake2s hash is" + " " + bl2.hexdigest(), font="Helvetica 12 italic", fg="green")
def shake128f():
    sh128=h.shake_128()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh128.update(d)
            l3.config(text="shake128 hash is" + " " + sh128.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha3384f():
    sh33=h.sha3_384()
    with open(fil, buffering=0, mode="rb") as ak:
        while True:
            d = ak.read(buf)
            if not d:
                break
            sh33.update(d)
            l3.config(text="sha3_384 hash is" + " " + sh33.hexdigest(), font="Helvetica 12 italic", fg="green")
def sha256f():
    sha256=h.sha256()
    with open(fil, buffering=0, mode="rb") as ak:
                while True:
                    d = ak.read(65536)
                    if not d:
                        break
                    sha256.update(d)
                    l3.config(text="SHA 256 hash is"+" "+sha256.hexdigest(),font="Helvetica 12 italic",fg="green")
def file1():
           global fil
           print(c8)
           if(c8==1):
               if (c.get() == "md5"):md5f()
               elif (c.get() == "sha224"):sha224f()
               elif (c.get() == "sha1"):sha1f()
               elif (c.get() == "blake2b"):blake2bf()
               elif (c.get() == "sha384"):sha384f()
               elif (c.get() == "sha3_512"):sha3512f()
               elif (c.get() == "sha3_256"):sha3256f()
               elif (c.get() == "shake_256"):shake256f()
               elif (c.get() == "sha3_224"):sha3224f()
               elif (c.get() == "sha512"):sha512f()
               elif (c.get() == "blake2s"):blake2sf()
               elif (c.get() == "shake_128"):shake128f()
               elif (c.get() == "sha3_384"):sha3384f()
               elif (c.get() == "sha256"):sha256f()
               else:pass
def file2():
    global c8,fil
    c8=1
    fil=filedialog.askopenfilename(initialdir="/",title="Browse for files",filetypes=(("All files","*.*"),("exe Files",".exe")))
    file1()
def has1():
    print(len(k.get()))
    r=k.get().encode()
    if(c.get()=="md5"):l3.config(text="Hash is :"+h.md5(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha224"):l3.config(text=h.sha224(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha1"):l3.config(text=h.sha1(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="blake2b"):l3.config(text=h.blake2b(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha384"):l3.config(text=h.sha384(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha3_512"):l3.config(text=h.sha3_512(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha3_256"):l3.config(text=h.sha3_256(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="shake_256"):l3.config(text=h.shake_256(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha3_224"):l3.config(text=h.sha3_224(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha512"):l3.config(text=h.sha512(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="blake2s"):l3.config(text=h.blake2s(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="shake_128"):l3.config(text=h.shake_128(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha3_384"):l3.config(text=h.sha3_384(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    elif(c.get()=="sha256"):l3.config(text=h.sha256(r).hexdigest(),font="Helvetica 12 italic",fg="green")
    else:pass
def men(event):
    global r
    l.config(text="Hashing Using"+"  "+c.get(),font="Helvetica 13 bold",fg="red")
    #t1=threading.Thread(target=has1())
    print(c.get())
    #t1.start()
    has1()
    file1()
def main12():
    global c,k,l1,l3
    k=tkinter.StringVar()
    c=ttk.Combobox(win,values=list(h.algorithms_guaranteed))
    c.current(0)
    print(h.algorithms_available)
    c.bind("<<ComboboxSelected>>",men)
    c.pack()
    l2=tkinter.Label(text="Enter your data here to hash",font="Helevetica 15 italic",fg="blue").pack()
    e=tkinter.Entry(win,textvariable=k)
    e.pack()
    f=ttk.Button(text="file",command=file2)
    f.pack()
    l1=tkinter.Label(text='')
    l1.pack()
    l3=tkinter.Label(text='')
    l3.pack()
win=tkinter.Tk()
win.title("Hashing")
buf=65536
l=tkinter.Label(text='')
l.pack()
t1=threading.Thread(target=main12())
t1.start()
b=ttk.Button(text="Hash",command=has1)
b.pack()
win.mainloop()
