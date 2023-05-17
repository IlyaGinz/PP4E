from tkinter import *

def showPostEvent(event):
    print(f'Widget={event.widget}, X={event.x}, Y={event.y}')

def showAllAvent(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))

def onKeyPress(event):
    print('Got key press:', event.char)


def onArrowPress(event):
    print('Got up arrow key press:', event.char)

def onReturnPress(event):
    print('Got up return key press:', event.char)

def onLeftClick(event):
    print('Got left mouse bottom click:', event.char, end=' ')
    showPostEvent(event)

def onRightClick(event):
    print('Got right mouse bottom click:', event.char, end=' ')
    showPostEvent(event)

def onMiddleClick(event):
    print('Got middle mouse bottom click:', event.char, end=' ')
    showPostEvent(event)
    showAllAvent(event)

def onLeftDrag(event):
    print('Got left mouse bottom drag:', event.char, end=' ')
    showPostEvent(event)

def onDoubleLeftClick(event):
    print('Got double left mouse click:', event.char, end=' ')
    showPostEvent(event)
    tkroot.quit()

tkroot = Tk()
labelfont = ('courier', 20, 'bold')
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)
widget.config(height=5, width=20)
widget.pack(expand=YES, fill=BOTH)
widget.bind('<Button-1>', onLeftClick)
widget.bind('<Button-3>', onRightClick)
widget.bind('<Button-2>', onMiddleClick)
widget.bind('<Double-1>', onDoubleLeftClick)
widget.bind('<B1-Motion>', onLeftDrag)
widget.bind('<KeyPress>', onKeyPress)
widget.bind('<Up>', onArrowPress)
widget.bind('<Return>', onReturnPress)
widget.focus()

tkroot.title('Click me')
tkroot.mainloop()



