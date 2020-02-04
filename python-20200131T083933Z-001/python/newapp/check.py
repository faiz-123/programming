from tkinter import *


def get():
    print(et.get())


root = Tk()

et =Entry(root,text="")
et.pack()
t = Button(root,command=get)
t.pack()

root.mainloop()
