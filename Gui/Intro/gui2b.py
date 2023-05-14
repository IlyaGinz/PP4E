import sys
from tkinter import *

root=Tk()
widget = Button(root, text='press', command=root.quit)
widget.pack(side=LEFT, expand=YES)
root.mainloop()
