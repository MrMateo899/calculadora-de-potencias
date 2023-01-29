from tkinter import *

def potenciar():
    res.set( float(bas.get() ** float(exp.get())))
    limpiar()

def limpiar():
    bas.set('')
    exp.set('')


root = Tk()
root.config(bd=15)

bas = StringVar()
exp = StringVar()
res = StringVar()

titulo = Label(root, text='BASE')
titulo.pack()
entr = Entry(root, justify='center', textvariable=bas)
entr.pack()

titulo1 = Label(root, text='EXPONENTE')
titulo1.pack()
entr1 = Entry(root, justify='center', textvariable=exp)
entr1.pack()

titulo2 = Label(root, text='POTENCIA')
titulo2.pack()
entr2 = Entry(root, justify='center', textvariable=res)
entr2.pack()

boton = Button(root, text='PORENCIAR', command=potenciar)
boton.pack

root.mainloop()