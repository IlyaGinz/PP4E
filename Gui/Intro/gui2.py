import sys
from tkinter import *

root=Tk()
widget = Button(root, text='Hello, GUI world!', command=sys.exit)
widget.pack()
root.mainloop()
