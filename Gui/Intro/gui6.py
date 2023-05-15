from tkinter import *


class Hello(Frame):
    def __init__(self, parent=None, **config):
        Frame.__init__(self, parent, **config)
        self.pack()
        self.data= 42
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Hello Frame world!', command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data += 1
        print(f'Hello frame world {self.data}')


if __name__ == '__main__':
    root = Tk()
    Hello(root)
    Hello(root)
    root.mainloop()
