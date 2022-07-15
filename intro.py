from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')  # Ancho y alto

l1 = label = Label(root, text='Hola mundo! mi primera etiqueta')
l2 = label = Label(root, text='Chao mundo! mi segunda etiqueta')
l3 = label = Label(root, text='----')
# Label(root, text='Hola mundo mi primera etiqueta').pack()

l1.grid(row=0, column=0)
l3.grid(row=1, column=1)
l2.grid(row=10, column=10)


root.mainloop()
