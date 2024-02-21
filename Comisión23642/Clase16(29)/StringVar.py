from tkinter import *
v0=Tk()#VENTANA PRINCIPAL
v0.geometry("200x200")
def cambiar_stringVar(nuevoTexto,MiTexto):
    MiTexto.set(nuevoTexto)
MiTexto=StringVar()
textoEntry=StringVar()
textVar=StringVar()
entry1=Entry(v0,textoEntry).pack()
label1=Label(v0,textVar,MiTexto).pack()
b1=Button(v0,text="ingrese texto",command=lambda: cambiar_stringVar(textoEntry.get(),MiTexto)).pack
    