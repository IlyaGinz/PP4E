from tkinter import *


class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('Goodbye subclass world')
        self.quit()

class SecondBuff(HelloButton):
    def callback(self):
        print('Second button pressed')

class ThemedButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=3)

def onSpam():
        print('OnSpam')

if __name__ == '__main__':
    root = Tk()
    HelloButton(root,text='Hello subclass world', bg='yellow')
    SecondBuff(root, text='2.nd', bg='white')
    B1 = ThemedButton(root, text='spam', command=onSpam)
    B2 = ThemedButton(root, text='eggs')
    B2.pack(expand=YES, fill=BOTH)
    root.mainloop()
