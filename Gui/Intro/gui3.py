import sys
from tkinter import *

def quit():
    print('Hello, I am going..')
    sys.exit()

root=Tk()
widget = Button(root, text='Hello even world!', command=quit)
widget.pack()
root.mainloop()
