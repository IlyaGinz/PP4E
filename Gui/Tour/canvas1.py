from tkinter import *

canvas = Canvas(width=525, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_line(100, 100, 200, 200)              # fromX, fromY, toX, toY
canvas.create_line(100, 200, 200, 300)
for i in range(1, 20, 2):
    canvas.create_line(0, i, 50, i)

canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')         # противоположные углы овала
canvas.create_arc(200, 200, 300, 100)                              # противоположные углы дуги
canvas.create_rectangle(200, 200, 300, 300, width=5, fill='red')   # противоположные углы рпямоугольника
canvas.create_line(0, 300, 150, 150, width=10, fill='green')

photo = PhotoImage(file='./../images/rora-lp4e.gif')
canvas.create_image(325, 25, image=photo, anchor=NW)               # верхний левый угол

widget = Label(canvas, text='Spam', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)                      # верхний левый угол

canvas.create_text(100, 280, text='Ham')                           # верхний левый угол

mainloop()