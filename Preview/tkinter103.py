from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='HellButton pressed!')

if __name__=='__main__':
    window= MyGui()
    window.pack()
    window.mainloop()

