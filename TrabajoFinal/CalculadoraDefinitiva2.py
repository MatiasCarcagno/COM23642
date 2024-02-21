from tkinter import *
from tkinter import ttk
import math

#Funcion para el tema noche
def TemaNoche(*args):
    estilos.configure("mainframe.TFrame", background="#010924")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#010924", foreground="white")
    estilos_label2.configure("Label2.TLabel", background="#010924", foreground="white")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#00044A", foreground="white") #Color de fondo y de los números
    estilos_botones_numeros.map("Botones_numero.TButton", background=[("active", "#020A90")]) #Color de fondo cuando pase el cursor por encima

    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#010924", foreground="white")
    estilos_botones_borrar.map("Botones_borrar.TButton", background=[("active", "#000AB1")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#010924", foreground="white")
    estilos_botones_restantes.map("Botones_restantes.TButton", background=[("active", "#000AB1")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#000000", foreground="white")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#000AB1")])

def TemaDia(*args):
    estilos.configure("mainframe.TFrame", background="#B2FCFF", foreground="black")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#B2FCFF", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#B2FCFF", foreground="black")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#51C3CC", foreground="black")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#ADD8E6")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#1E8E99", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#B22222")], background=[("active", "#ADD8E6")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#1E8E99", foreground="black")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#ADD8E6")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#006666", foreground="black")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#ADD8E6")])



#Función para el tema clasico
def TemaClasico(*args):
    estilos.configure("mainframe.TFrame", background="#DBDBDB", foreground="black")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#DBDBDB", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#DBDBDB", foreground="black")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#B9B9B9")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#CECECE", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#FF0000")], background=[("active", "#858585")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#CECECE", foreground="black")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#858585")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#AFB5B8", foreground="black")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#858585")])

def TemaOrange(*args):
    estilos.configure("mainframe.TFrame", background="#F5A746", foreground="black")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#F5A746", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#F5A746", foreground="black")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#F2862C", foreground="black")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#FBBC70")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#ED7222", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#B71D3E")], background=[("active", "#FBBC70")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#ED7222", foreground="black")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#FBBC70")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#D35400", foreground="black")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#FBBC70")])

def TemaYellow(*args):
    estilos.configure("mainframe.TFrame", background="#F2F483", foreground="black")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#F2F483", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#F2F483", foreground="black")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#F6D442", foreground="black")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#FCFFA4")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#FCB216", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#B71D3E")], background=[("active", "#FCFFA4")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#FCB216", foreground="black")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#FCFFA4")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#FFC000", foreground="black")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#FCFFA4")])

def TemaGreen(*args):
    estilos.configure("mainframe.TFrame", background="#50FF50", foreground="black")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#50FF50", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#50FF50", foreground="black")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#00F100", foreground="black")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#86FF86")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#55BF3B", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#B71D3E")], background=[("active", "#86FF86")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#55BF3B", foreground="black")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#86FF86")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#008600", foreground="black")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#86FF86")])

def TemaRed(*args):
    estilos.configure("mainframe.TFrame", background="#EC4540", foreground="white")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#EC4540", foreground="white")
    estilos_label2.configure("Label2.TLabel", background="#EC4540", foreground="white")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#E8201D", foreground="white")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#EF6A63")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#DF0000", foreground="white")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#B71D3E")], background=[("active", "#EF6A63")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#DF0000", foreground="white")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#EF6A63")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#7F0000", foreground="white")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#EF6A63")])

def TemaPurple(*args):
    estilos.configure("mainframe.TFrame", background="#713585", foreground="white")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#713585", foreground="white")
    estilos_label2.configure("Label2.TLabel", background="#713585", foreground="white")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#4C205F", foreground="white")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#8F5EA0")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#270B3A", foreground="white")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "#B71D3E")], background=[("active", "#8F5EA0")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#270B3A", foreground="white")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#8F5EA0")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#49006A", foreground="white")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#8F5EA0")])

def TemaMulticolor(*args):
    estilos.configure("mainframe.TFrame", background="#33FF00", foreground="black")#Color de fondo del frame y de los números

    estilos_label1.configure("Label1.TLabel", background="#33FF00", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#33FF00", foreground="black")

    estilos_botones_numeros.configure("Botones_numero.TButton", background="#FF0000", foreground="black")
    estilos_botones_numeros.map("Botones_numero.TButton",background=[("active", "#0033FF")]) 
    
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#FFFF00", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton",foreground=[("active", "white")], background=[("active", "#FF00CC")])

    estilos_botones_restantes.configure("Botones_restantes.TButton", background="#00FFFF", foreground="black")
    estilos_botones_restantes.map("Botones_restantes.TButton",background=[("active", "#FF9900")])

    estilos_botones_funciones.configure("Botones_funciones.TButton", background="#FF00CC", foreground="black")
    estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#FFFF00")])

# Función para ingresar los distintos valores
def IngresarValores(tecla):

    # Verificar si la tecla es un dígito o uno de los caracteres permitidos
    if tecla.isdigit() or tecla in "()." :
        entrada2.set(entrada2.get() + tecla)  # Agregar a la entrada2

    
    # Verificar si la tecla es uno de los operadores *-+/
    elif tecla in "*/+-**":
        entrada2.set(entrada2.get() + tecla)  # Agregar a la entrada2

    elif tecla in "πeTAns":
        if tecla == "π":
            entrada2.set(entrada2.get() + f"{math.pi}")
        elif tecla == "e":  
            entrada2.set(entrada2.get() + f"{math.e}")
        elif tecla == "T":
            entrada2.set(entrada2.get() + f"{math.tau}")
        elif tecla == "Ans":
            entrada2.set(resultadoAns.get())
            
                     
    # Verificar si la tecla es el signo igual
    elif tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())  # Concatenar entrada actual (entrada2) a entrada1 (arriba)
        try:
            resultado = eval(entrada1.get())  # Evaluar la expresión matemática en entrada1
            entrada2.set(resultado) # Mostrar el resultado en entrada2 si es correcto
            if tecla == "Ans":
                resultadoAns.set(f"Ans {resultado}")
        except Exception as e:
            entrada2.set("Error")  # Si hay algún error en la operación, mostrar "Error"
    
    
        
        
def IngresarPorTeclado(evento):
    tecla = evento.char #Devuelve el caracter asociado al momento de apretar el teclado
    
    if tecla: #Se verifica si la tecla tiene algún valor
        IngresarValores(tecla)# se llama a la funcion de ingresar valores para los demas caracteres que serán ingresados

#Funcion borrar de a un caracter
# La función acepta un parámetro llamado evento, el cual es opcional y tiene un valor predeterminado de una cadena vacía ("")
#En la funcion este ultimo parametro no se utiliza, lo colocamos para la extensión de la función que permite borrar con la tecla "b"
#Obtenemos el texto de la entrada2 y despues a traves de "[:-1]" se devuelven todos los caracteres excepto el último 
def borrar(evento=""):#
    entrada2.set(entrada2.get()[:-1])

#Funcion de borrar todo, simplemente dejamos las dos entradas como cadenas vacias
def borrarTodo():
    entrada1.set("")
    entrada2.set("")

#Funciones operaciones:
#Antes de calcular cada función trigonométrica o exponencial, se toma el valor actual en entrada2 y se almacena en la variable operacion. 
#En la variable resultado, se establece la función para resolver la operacion
#Después, se establece entrada1 con la operación correspondiente y entrada2 con el resultado.
# El except maneja la excepción ValueError que podría ocurrir si la conversión a float no es posible, estableciendo entrada2 como "Error"
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
        operacion = float (entrada2.get())
        resultado = math.sin(math.radians(operacion))
        entrada1.set(f"sin({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def coseno():
    try:
        operacion = float (entrada2.get())
        resultado = math.cos(math.radians(operacion))
        entrada1.set(f"cos({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def tangente():
    try:
        operacion = float(entrada2.get())
        resultado = math.tan(math.radians(operacion))
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
    except:
        entrada2.set("Error")
        

def logaritmo():
    try:
        operacion = entrada2.get()
        resultado = math.log(float(operacion))
        entrada1.set(f"in({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")
        

def logaritmo10():
    try:
        operacion = entrada2.get()
        resultado = math.log10(float(operacion))
        entrada1.set(f"log({operacion})")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")
    
                       
            #CREAMOS LA VENTANA RAÍZ DE LA APLICACIÓN:
root = Tk() 
root.title("Calculadora científica")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)#La ventana se posiciona en las coordenadas x=500 y y=80 en la pantalla
root.rowconfigure(0, weight=1)#Configuramos el peso de la unica fila y columna de la ventana
# Esto significa que la ventana se expandirá o contraerá proporcionalmente cuando se cambie el tamaño


                        # CONFIGURAMOS EL ESTILO DE LA PANTALLA:
estilos = ttk.Style()
estilos.theme_use("alt")#Elegimos el tema
estilos.configure("mainframe.TFrame", background="#B2FCFF") # Configuramos el estilo del marco principal con la etiqueta "mainframe.TFrame"
# Elegimos el color del fondo a través del "background"

                        # CREACIÓN DEL MARCO PRINCIPAL:
mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W,N,E,S)) #Utilizamos el metodo grid para colocar el marco en la ventana raiz (root)


                        # ASIGNACIÓN DE "COLUMNS" Y "ROWS" EN LA VENTANA RAIZ:
for i in range(6): # El bucle for itera sobre las primeras 5 columnas del marco principal (índices 0, 1, 2, 3, 4).
    mainframe.columnconfigure(i, weight=1) # "i" es el índice de la columna que se está configurando
for i in range(8):
    mainframe.rowconfigure(i, weight=1)

                        # DEFINICIÓN Y CONFIGURACIÓN DE LOS ESTILOS DE WIDGETS A USAR COMO "DISPLAYS":
estilos_label1 = ttk.Style()
estilos_label1.configure("Label1.TLabel", font="arial 15", anchor="e", background="#B2FCFF")

estilos_label2 = ttk.Style()
estilos_label2.configure("Label2.TLabel", font="arial 40", anchor="e", background="#B2FCFF")

                        # DECLARAMOS VARIABLES DE ENTRADA Y LAS CONFIGURAMOS:
# La variable de tipo StringVar, permite almacenar y reastrear datos de cadena para vincular al widget a datos que pueden cambiar
#Creamos un widget de tipo label dentro del marco principal
#Viculamos la variable entrada1 a la etiqueta, esto hace que cualquier cambio en entrada1 se vea reflejado en la etiqueta
#Luego colocamos la etiqueta en la ventana 
entrada1 = StringVar() 
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel") 
label_entrada1.grid(column=0, row=0, columnspan=6, sticky=(N, E, S, W))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=6, sticky=(N, E, S, W))

resultadoAns = StringVar()
label_resultadoAns = ttk.Label(mainframe, textvariable=resultadoAns, style="Label2.TLabel")
label_resultadoAns.grid(column=0, row=0, sticky=(E))



                        # CONFIGURAMOS EL ESTILO PARA LOS BOTONES NUMÉRICOS Y DE MANDO:
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("Botones_numero.TButton", font="arial 22", width=5, background="#51C3CC", relief="flat")
estilos_botones_numeros.map("Botones_numero.TButton", background=[("active", "#ADD8E6")]) # Permite asignar estilos diferentes para diferentes estados del widget
                        
estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("Botones_borrar.TButton", font="arial 22", width=5, background="#1E8E99", relief="flat")
estilos_botones_borrar.map("Botones_borrar.TButton", foreground=[("active", "#B22222")], background=[("active", "#ADD8E6")])

estilos_botones_funciones = ttk.Style()
estilos_botones_funciones.configure("Botones_funciones.TButton", font="arial 22", width= 5, background="#006666", relief="flat")
estilos_botones_funciones.map("Botones_funciones.TButton", background=[("active", "#ADD8E6")])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure("Botones_restantes.TButton", font="arial 22", width=5, background="#1E8E99", relief="flat")
estilos_botones_restantes.map("Botones_restantes.TButton", background=[("active", "#ADD8E6")])

                       
                        # DEFINIMOS LOS BOTONES NUMÉRICOS Y DE COMANDO:
# Se aplica el estilo "Botones_numero.TButton" y se asocia la función IngresarValores("0") al evento... 
#BOTONES NUMÉRICOS:                                                                 ...de clic del botón
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

#BOTONES DE COMANDOS BÁSICOS:
#utilizamos el valor chr(9003) para representar una flecha de retroceso.
boton_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
boton_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrarTodo())
boton_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: IngresarValores("("))
boton_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: IngresarValores(")"))
boton_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: IngresarValores("."))
boton_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: IngresarValores("="))

#COMANDOS ESPECIALES:
boton_ans = ttk.Button(mainframe, text="Ans", style="Botones_restantes.TButton", command=lambda: IngresarValores("Ans"))

#OPERACIONES BÁSICAS:
boton_division = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda: IngresarValores("/"))
boton_multi = ttk.Button(mainframe, text="x", style="Botones_restantes.TButton", command=lambda: IngresarValores("*"))
boton_suma = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: IngresarValores("+"))
boton_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: IngresarValores("-"))

#OPERACIONES NO TAN BÁSICAS:
boton_porcentaje = ttk.Button(mainframe, text="%", style="Botones_restantes.TButton", command=lambda: porcentaje())
boton_raiz_cuadrada = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda: raizCuadrada())
boton_potencia = ttk.Button(mainframe, text="^", style="Botones_restantes.TButton", command=lambda: IngresarValores("**"))


#BOTONES DE VALORES PRE-ESTABLECIDOS:
boton_pi = ttk.Button(mainframe, text="π", style="Botones_restantes.TButton", command=lambda: IngresarValores("π"))
boton_e = ttk.Button(mainframe, text="e", style="Botones_restantes.TButton", command=lambda: IngresarValores("e"))
boton_T = ttk.Button(mainframe, text="T", style="Botones_restantes.TButton", command=lambda: IngresarValores("T"))


#FUNCIONES TRIGONOMÉTRICAS:
boton_seno = ttk.Button(mainframe, text="sin", style="Botones_funciones.TButton", command=lambda: seno())
boton_coseno = ttk.Button(mainframe, text="cos", style="Botones_funciones.TButton", command=lambda: coseno())
boton_tangente = ttk.Button(mainframe, text="tan", style="Botones_funciones.TButton", command=lambda: tangente())
boton_exponencial = ttk.Button(mainframe, text="exp", style="Botones_funciones.TButton", command=lambda: exponencial())
boton_log = ttk.Button(mainframe, text="in", style="Botones_funciones.TButton", command=lambda: logaritmo())
boton_log10 = ttk.Button(mainframe, text="log", style="Botones_funciones.TButton", command=lambda: logaritmo10())


# BOTONES.GRID, DIBUJAMOS LOS BOTONES INTERACTIVOS:

#FILA 2:
boton_parentesis1.grid(column=0, row=2, sticky=(W,N,E,S))
boton_parentesis2.grid(column=1, row=2, sticky=(W,N,E,S))
boton_borrar_todo.grid(column=2, row=2, sticky=(W,N,E,S))
boton_borrar.grid(column=3, row=2, columnspan=2, sticky=(W,N,E,S))

#FILA 3:
boton7.grid(column=0, row=3, sticky=(W,N,E,S))
boton8.grid(column=1, row=3, sticky=(W,N,E,S))
boton9.grid(column=2, row=3, sticky=(W,N,E,S))
boton_division.grid(column=3, row=3, sticky=(W,N,E,S))

#FILA 4:
boton4.grid(column=0, row=4, sticky=(W,N,E,S))
boton5.grid(column=1, row=4, sticky=(W,N,E,S))
boton6.grid(column=2, row=4, sticky=(W,N,E,S))
boton_multi.grid(column=3, row=4, sticky=(W,N,E,S))

#FILA 5:
boton1.grid(column=0, row=5, sticky=(W,N,E,S))
boton2.grid(column=1, row=5, sticky=(W,N,E,S))
boton3.grid(column=2, row=5, sticky=(W,N,E,S))
boton_suma.grid(column=3, row=5, sticky=(W,N,E,S))

#FILA 6:
boton0.grid(column=0, row=6, sticky=(W,N,E,S))
boton_punto.grid(column=1, row=6, columnspan=2, sticky=(W,N,E,S))
boton_resta.grid(column=3, row=6, sticky=(W,N,E,S))

#FILA 7:
boton_igual.grid(column=0, row=7, columnspan=2, sticky=(W,N,E,S))
boton_ans.grid(column=2, row=7, sticky=(W,N,E,S))
boton_pi.grid(column=3, row=7, sticky=(W,N,E,S))

#COLUMNA 4:
boton_raiz_cuadrada.grid(column=4, row=3, sticky=(W,N,E,S))
boton_porcentaje.grid(column=4, row=5, sticky=(W, N, E, S))
boton_e.grid(column=4, row=6, sticky=(W,N,E,S))
boton_T.grid(column=4, row=7, sticky=(W, N, E, S))


#COLUMNA 5:
boton_log10.grid(column=5, row=2, sticky=(W,N,E,S))
boton_log.grid(column=5, row=3, sticky=(W,N,E,S))
boton_seno.grid(column=5, row=4, sticky=(W,N,E,S))
boton_coseno.grid(column=5, row=5, sticky=(W,N,E,S))
boton_tangente.grid(column=5, row=6, sticky=(W,N,E,S))
boton_exponencial.grid(column=5, row=7, sticky=(W,N,E,S))


#COLUMNA 6:
boton_potencia.grid(column=4, row=4, sticky=(W, N, E, S))


#Configuramos ciertos parametros de diseño de los widgets hijos del widget padre (mainframe)
#Iniciamos un bucle que itera a través de todos los widgets hijos del marco principal
#mainframe.winfo_children() devuelve una lista que contiene todos los widgets hijos de mainframe
#child.grid_configure(ipady=10, padx=1, pady=1): Configuramos ciertos parámetros de diseño para cada widget hijo
#ipady=10: establece espacio vertical interno de 10 pixeles en los widgets
#padx=1:establece un espacio horizontal externo de 1 pixel entre los widgets
#pady=1: establece un espacio vertical externo de 1 pixel entre los widgets 
for child in mainframe.winfo_children(): 
    child.grid_configure(ipady=10, padx=2, pady=0.5)

#A traves de root.bind vinculamos eventos del teclado para que se ejecuten las funciones al presionar sus respectivas teclas
root.bind("<KeyPress-n>", TemaNoche)
root.bind("<KeyPress-d>", TemaDia)
root.bind("<KeyPress-c>", TemaClasico)
root.bind("<KeyPress-o>", TemaOrange)
root.bind("<KeyPress-y>", TemaYellow)
root.bind("<KeyPress-g>", TemaGreen)
root.bind("<KeyPress-r>", TemaRed)
root.bind("<KeyPress-p>", TemaPurple)
root.bind("<KeyPress-m>", TemaMulticolor)
root.bind("<Key>", IngresarPorTeclado)
root.bind("<KeyPress-B>", borrar)
root.bind("<KeyPress-b>", borrar)

root.mainloop()