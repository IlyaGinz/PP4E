import sys
from tkinter import *

class HelloClass:
    def __init__(self, root):
        self.root = root
        widget = Button(self.root, text='Hello Class event world!', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello, class world!')
        sys.exit()


root=Tk()
HelloClass(root)
root.mainloop()
