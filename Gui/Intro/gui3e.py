import sys
from tkinter import *

def hello(event):
    print('Press twice to exit')

def quit(event):
    print('Hello,I must be going..')
    sys.exit()


root=Tk()
widget = Button(root, text='Hello Event world!')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
root.mainloop()
