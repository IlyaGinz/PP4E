from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda : askquestion('Warning', 'You typed "rm *"\nConfirm?'),
    'Error': lambda : showerror('Error!', "He's dead, Jim"),
    'Input': lambda : askfloat('Entry', "enter creadit card nubmer"),
    'Save': asksaveasfile
}