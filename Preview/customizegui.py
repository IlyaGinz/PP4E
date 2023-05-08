from tkinter import *
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def reply(selfself):
        showinfo(title='popup', message='Ouch!')

if __name__=='__main__':
    CustomGui().pack()
    mainloop()