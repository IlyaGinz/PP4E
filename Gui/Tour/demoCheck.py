from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        Label(self, text='Check demos').pack()
        self.vars = []
        for key in demos:
            var = IntVar()
            Checkbutton(self, text=key, variable=var, command=demos[key]).pack(side=LEFT)

        Quitter(self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        print(name, 'returns =>', demos[name]())

if __name__=='__main__': Demo().mainloop()