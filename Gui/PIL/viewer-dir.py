import os, sys
from tkinter import *
from PIL import Image, ImageTk
#from ImageTk import Image


imgdir = '../images'
if len(sys.argv) > 1: imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)
print(imgfiles)

main = Tk()
main.title('Viewer')
quit = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quit.pack()

savephotos = []
for imgfile in imgfiles:
    imgpath = os.path.join(imgdir, imgfile)
    #print(imgpath)
    win = Toplevel()
    win.title(imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())
        savephotos.append(imgobj)
    except:
        errmsg = f'skipping {imgfile}\n{sys.exc_info()[1]}'
        Label(win, text=errmsg).pack()

main.mainloop()