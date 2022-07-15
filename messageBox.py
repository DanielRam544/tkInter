from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')


# def click():
#     messagebox.showwarning('Popup', 'Hola mundo;')

# def click():
#     messagebox.showinfo('Popup', 'Hola mundo;')

# def click():
#     messagebox.showerror('Popup', 'Hola mundo;')

# def click():
#     respuesta = messagebox.askquestion('Popup', 'Hola mundo;')
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
#     else:
#         messagebox.showwarning('Respuesta', 'la respuesta fue ' + respuesta)

# def click():
#     respuesta = messagebox.askokcancel(
#         'Hola mundo ', 'deseas realizar accion ')
#     if respuesta:
#         messagebox.showinfo('Hola mundo ', 'La respuesta fue ok')
#     else:
#         messagebox.showerror('Hola mundo', 'La respuesta fuew no')

def click():
    respuesta = messagebox.askyesno(
        'Hola mundo ', 'deseas realizar accion ')
    if respuesta:
        messagebox.showinfo('Hola mundo ', 'La respuesta fue ok')
    else:
        messagebox.showerror('Hola mundo', 'La respuesta fuew no')


btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()
