from tkinter import *
from tkinter import ttk
import math

#Funcion para el tema oscuro
def TemaOscuro(*args):
    estilos.configure("mainframe.TFrame", background="#010924")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#010924", foreground="white")
    estilos_label2.configure("Label2.TLabel", background="#010924", foreground="white")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#00044A", foreground="white") #Color de fondo y de los números
    estilos_botones_numeros.map("Botones_numero.TButton", background=[("active", "#020A90")]) #Color de fondo cuando pase el cursor por encima

    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#010924", foreground="white")
    estilos_botones_borrar.map("Botones_borrar.TButton", background=[("active", "#000AB1")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#010924", foreground="white")
    estilos_botones_restantes.map("Botones_restantes.TButton", background=[("active", "#000AB1")])

#Función para el tema claro
def TemaClaro(*args):
    estilos.configure("mainframe.TFrame", background="#DBDBDB", foreground="black")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#DBDBDB", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#DBDBDB", foreground="black")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#B9B9B9")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#CECECE", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#FF0000")], background=[("active", "#858585")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#CECECE", foreground="black")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#858585")])

#Funcion para ingresar los distintos valores 
def IngresarValores(tecla):
    if tecla.isdigit() or tecla in "().": #Verificar si la tecla es un digito o uno de los carecteres permitidos
        entrada2.set(entrada2.get() + tecla) #Si es correcto se agrega a la entrada2, parte de abajo

    if tecla in "*/+-": #Lo mismo para los operadores *-+/
        entrada2.set(entrada2.get() + tecla)

    if tecla == "=": #Verifica si es el signo igual
        entrada1.set(entrada1.get() + entrada2.get()) #Si es asi concatena la entrada actual (entrada2) a la entrada1 (la línea de entrada de arriba).
        try:
            resultado = eval(entrada1.get()) #Con "eval" se evalua la expresión matematica en la entrada1
            entrada2.set(resultado) #Se muestra el resultado en la entrada2 en el caso que sea correcta
        except Exception as e:
            entrada2.set("Error")#Si hay algun error en la operación, muestra "Error"

def IngresarPorTeclado(momento):
    tecla = momento.char #Devuelve el caracter asociado al momento de apretar el teclado
    
    if tecla: #Se verifica si la tecla tiene algún valor
        if tecla.lower() == "o": #Si es "o" se activa la funcion para el tema oscuro
            TemaOscuro()
        elif tecla.lower() == "c":#Si es "c" se activa la funcion para el tema claro
            TemaClaro()
        else:
            IngresarValores(tecla)#Si no es "o" ni "c" se llama a la funcion de ingresar valores para los demas caracteres que serán ingresados


def borrar(momento=""):
    entrada2.set(entrada2.get()[:-1])

def borrarTodo():
    entrada1.set("")
    entrada2.set("")

def raizCuadrada():
    try:
        operacion = entrada2.get()
        resultado = math.sqrt(float(operacion))
        entrada1.set(f"√{operacion}")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def seno():
    try:
        operacion = entrada2.get()
        resultado = math.sin(float(operacion))
        entrada1.set(f"sin({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def coseno():
    try:
        operacion = entrada2.get()
        resultado = math.cos(float(operacion))
        entrada1.set(f"cos({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def tangente():
    try:
        operacion = entrada2.get()
        resultado = math.tan(float(operacion))
        entrada1.set(f"tan({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def exponencial():
    try:
        operacion = entrada2.get()
        resultado = math.exp(float(operacion))
        entrada1.set(f"exp({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def porcentaje():
    entrada1.set(entrada2.get() + "/100")
    try:
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
    except Exception as e:
        entrada2.set("Error")

root = Tk()
root.title("Calculadora científica")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W,N,E,S))
for i in range(4):
    mainframe.columnconfigure(i, weight=1)
for i in range(8):
    mainframe.rowconfigure(i, weight=1)

estilos_label1 = ttk.Style()
estilos_label1.configure("Label1.TLabel", font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure("Label2.TLabel", font="arial 40", anchor="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=5, sticky=(N, E, S, W))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=5, sticky=(N, E, S, W))

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("Botones_numero.TButton", font="arial 22", width=5, background="#FFFFFF", relief="flat")
estilos_botones_numeros.map("Botones_numero.TButton", background=[("active", "#B9B9B9")])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("Botones_borrar.TButton", font="arial 22", width=5, background="#CECECE", relief="flat")
estilos_botones_borrar.map("Botones_borrar.TButton", foreground=[("active", "#FF0000")], background=[("active", "#858585")])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure("Botones_restantes.TButton", font="arial 22", width=5, background="#CECECE", relief="flat")
estilos_botones_restantes.map("Botones_restantes.TButton", background=[("active", "#858585")])

boton0 = ttk.Button(mainframe, text="0", style="Botones_numero.TButton", command=lambda: IngresarValores("0"))
boton1 = ttk.Button(mainframe, text="1", style="Botones_numero.TButton", command=lambda: IngresarValores("1"))
boton2 = ttk.Button(mainframe, text="2", style="Botones_numero.TButton", command=lambda: IngresarValores("2"))
boton3 = ttk.Button(mainframe, text="3", style="Botones_numero.TButton", command=lambda: IngresarValores("3"))
boton4 = ttk.Button(mainframe, text="4", style="Botones_numero.TButton", command=lambda: IngresarValores("4"))
boton5 = ttk.Button(mainframe, text="5", style="Botones_numero.TButton", command=lambda: IngresarValores("5"))
boton6 = ttk.Button(mainframe, text="6", style="Botones_numero.TButton", command=lambda: IngresarValores("6"))
boton7 = ttk.Button(mainframe, text="7", style="Botones_numero.TButton", command=lambda: IngresarValores("7"))
boton8 = ttk.Button(mainframe, text="8", style="Botones_numero.TButton", command=lambda: IngresarValores("8"))
boton9 = ttk.Button(mainframe, text="9", style="Botones_numero.TButton", command=lambda: IngresarValores("9"))

boton_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
boton_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrarTodo())
boton_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: IngresarValores("("))
boton_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: IngresarValores(")"))
boton_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: IngresarValores("."))

boton_division = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda: IngresarValores("/"))
boton_multi = ttk.Button(mainframe, text="x", style="Botones_restantes.TButton", command=lambda: IngresarValores("*"))
boton_suma = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: IngresarValores("+"))
boton_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: IngresarValores("-"))

boton_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: IngresarValores("="))
boton_raiz_cuadrada = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda: raizCuadrada())
boton_seno = ttk.Button(mainframe, text="sin", style="Botones_restantes.TButton", command=lambda: seno())
boton_coseno = ttk.Button(mainframe, text="cos", style="Botones_restantes.TButton", command=lambda: coseno())
boton_tangente = ttk.Button(mainframe, text="tan", style="Botones_restantes.TButton", command=lambda: tangente())
boton_exponencial = ttk.Button(mainframe, text="exp", style="Botones_restantes.TButton", command=lambda: exponencial())
boton_porcentaje = ttk.Button(mainframe, text="%", style="Botones_restantes.TButton", command=lambda: porcentaje())

boton_parentesis1.grid(column=0, row=2, sticky=(W,N,E,S))
boton_parentesis2.grid(column=1, row=2, sticky=(W,N,E,S))
boton_borrar_todo.grid(column=2, row=2, sticky=(W,N,E,S))
boton_borrar.grid(column=3, row=2, columnspan=2, sticky=(W,N,E,S))

boton7.grid(column=0, row=3, sticky=(W,N,E,S))
boton8.grid(column=1, row=3, sticky=(W,N,E,S))
boton9.grid(column=2, row=3, sticky=(W,N,E,S))
boton_division.grid(column=3, row=3, sticky=(W,N,E,S))

boton4.grid(column=0, row=4, sticky=(W,N,E,S))
boton5.grid(column=1, row=4, sticky=(W,N,E,S))
boton6.grid(column=2, row=4, sticky=(W,N,E,S))
boton_multi.grid(column=3, row=4, sticky=(W,N,E,S))

boton1.grid(column=0, row=5, sticky=(W,N,E,S))
boton2.grid(column=1, row=5, sticky=(W,N,E,S))
boton3.grid(column=2, row=5, sticky=(W,N,E,S))
boton_suma.grid(column=3, row=5, sticky=(W,N,E,S))

boton0.grid(column=0, row=6, columnspan=2, sticky=(W,N,E,S))
boton_punto.grid(column=2, row=6, sticky=(W,N,E,S))
boton_resta.grid(column=3, row=6, sticky=(W,N,E,S))

boton_igual.grid(column=0, row=7, columnspan=3, sticky=(W,N,E,S))
boton_raiz_cuadrada.grid(column=3, row=7, sticky=(W,N,E,S))

boton_seno.grid(column=4, row=4, sticky=(W,N,E,S))
boton_coseno.grid(column=4, row=5, sticky=(W,N,E,S))
boton_tangente.grid(column=4, row=6, sticky=(W,N,E,S))
boton_exponencial.grid(column=4, row=7, sticky=(W,N,E,S))
boton_porcentaje.grid(column=4, row=3, sticky=(W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind("<KeyPress-o>", TemaOscuro)
root.bind("<KeyPress-c>", TemaClaro)
root.bind("<Key>", IngresarPorTeclado)
root.bind("<KeyPress-b>", borrar)
root.bind("<KeyPress-B>", borrar)

root.mainloop()