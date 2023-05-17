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
            self.vars.append(var)

    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')
            print()

    def tools(self):
        frm = Frame(self, bd=2, relief=GROOVE, padx=2, pady=2)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)

    
if __name__=='__main__': Demo().mainloop()