from tkinter import *

def greeting():
    print('Hello stdout world!')

root = Tk()
win = Frame(root, relief=GROOVE, bd=2)
win.pack(side=TOP, fill=BOTH, expand=YES)
Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
Label(win, text="Hello container world!").pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)
root.mainloop()
