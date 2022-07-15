from tkinter import *

root = Tk()
root.title('Hola mundo!')

# frame = LabelFrame(root, text='Login', padx=20, pady=20, borderwidth=10)
frame = LabelFrame(root, padx=20, pady=20, borderwidth=10)
frame.pack(padx=50, pady=50)

frame.pack()
l = Label(frame, text='Estoy dentro de un frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()
