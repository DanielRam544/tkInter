from tkinter import *

root = Tk()
root.title('Hola mundo!')

l = Label(root, text='Hola mundo')


def click():
    l.pack()


btn = Button(root, text='Clickeame', command=click, fg='white', bg='black')
btn.pack()

root.mainloop()
