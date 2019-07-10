from tkinter import *

win = Tk()
text = Label(win, text='Hello World', fg='red')
text.pack()
button = Button(win, text='Quitter', command=win.destroy)
button.pack()
win.mainloop()
