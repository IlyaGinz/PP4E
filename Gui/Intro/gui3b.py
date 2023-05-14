import sys
from tkinter import *

def quit():
    print('Hello, I am going..')
    sys.exit()

root=Tk()
widget = Button(root, text='Hello event world!', command=(lambda: print('Hello lambda world!') or sys.exit()))
widget.pack()
root.mainloop()
