from tkinter import *

class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(options)

    def handleList(self, event):
        #index = self.listbox.curselection()
        #label = self.listbox.get(index)

        label = self.listbox.get(ACTIVE)
        self.runCommand(label)

    def onDoubleClick(self):
        selections = self.list.curselection()
        selections = [int(x)+1 for x in selections]
        self.runCommand(selections)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        self.list = list
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)

        pos = 0
        for label in options:
            list.insert(pos, label)
            pos += 1

        #list.config(selectmode=SINGLE, setgrid=1)
        list.bind('<Double-1>', self.handleList)

        #list.config(selectmode=EXTENDED, setgrid=1)
        #list.bind('<Double-1>', (lambda event: self.onDoubleClick()))

        self.listbox = list

    def runCommand(self, selection):
        print('You selected', selection)

if __name__ == '__main__':
    options = (f'lumberjack-{x}' for x in range(20))
    ScrolledList(options).mainloop()
    