from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo!')

# imagen = Image.open('Foto1.jpg')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('Foto1.jpg'))
l = Label(image=img)
l.pack()

root.mainloop()
