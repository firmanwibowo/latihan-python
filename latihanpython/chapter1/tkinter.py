from Tkinter import *
master = Tk()
def text():
   print "MY NAME IS FIRMAN WIBOWO .!:P"
 
def text2():
   print "hey kamu juga mengklick diriku !dasar genitt:P"

title = Label(master, text="Tkinter Gui tutorial")
title.pack(side=TOP)
 
button1 = Button(master, text="klick MY NAME !", fg="red", command=text)
button1.pack(side=LEFT)
 
button2 = Button(master, text="klick sy juga!", fg="blue", command=text2)
button2.pack(side=RIGHT)
 
mainloop()
