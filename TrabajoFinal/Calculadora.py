from tkinter import *   # Importamos librerías a utilizar, Tkinter nos proporciona funciones de interfaz gráfica.
from tkinter import ttk # "ttk" es una extensión de la librería Tkinter, posee más opciones de comando.    
import math             # La librería "math" nos dá a acceso a funciones de cálculos matemáticos complejos.



# FUNCIONES QUE CONFIGURAN EL COLOR DE LA PANTALLA:
def TemaNoche(*args):
    # BackGround, ForeGround, Tipo del Frame :
    estilos.configure("mainframe.TFrame", background="#010924") 

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



# FUNCIÓN CALCULADORA:
def IngresarValores(tecla):

    if tecla.isdigit() or tecla in "()." :    # Distingue dígitos de operadores
        entrada2.set(entrada2.get() + tecla)  # Agrega a la entrada2

    elif tecla in "*/+-**":                   # Identifica operadores
        entrada2.set(entrada2.get() + tecla)  # Agrega a la entrada2

# INVOCAMOS LAS FUNCIONES DE MATH PARA OBTENER VALORES:
    elif tecla in "πeTAns":                   # Identifica valores
        if tecla == "π":
            entrada2.set(entrada2.get() + f"{math.pi}")  
        elif tecla == "e":  
            entrada2.set(entrada2.get() + f"{math.e}")
        elif tecla == "T":
            entrada2.set(entrada2.get() + f"{math.tau}")
        elif tecla == "Ans":
            entrada2.set(resultadoAns.get())
           
    elif tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())  # Concatenar entrada actual (entrada2) a entrada1 (arriba)
# UTILIZAMOS LA FUNCIÓN "try" PARA LA CALCULADORA:
        try:
            resultado = eval(entrada1.get())  # Evaluar la expresión matemática en entrada1
            entrada2.set(resultado)           # Mostrar el resultado en entrada2 si es correcto
            resultadoAns.set(resultado)       # Guarda el resultado en una StringVar() para poder reutilizarlo
        except Exception as e:
            entrada2.set("Error")             # Si hay algún error en la operación, mostrar "Error"
        
# FUNCIÓN PARA UTILIZAR EL TECLADO:
def IngresarPorTeclado(evento):
    tecla = evento.char           # Devuelve el caracter asociado al momento de apretar el teclado
    
    if tecla:                     # Se verifica si la tecla tiene algún valor
        IngresarValores(tecla)    # Se llama a la funcion de IngresarValores para los demas caracteres que serán ingresados

# FUNCIÓN BORRAR ÚLTIMO:
def borrar(evento=""):                 
    entrada2.set(entrada2.get()[:-1])  #Obtenemos el texto de la entrada2 y despues a traves de "[:-1]"...  
                                       # ...se devuelven todos los caracteres excepto el último  
                                          
# FUNCIÓN PARA LIMPIAR PANTALLA:
def borrarTodo():
    entrada1.set("")  # Le asignamos un parámetro vacío a las entradas
    entrada2.set("")

#FUNCIONES PARA OPERACIONES TRIGONOMÉTRICAS Y EXPONENCIALES:
def raizCuadrada():
    try:
        operacion = entrada2.get()              # Se guarda la entrada2 en la variable str, para poder ulizarla.
        resultado = math.sqrt(float(operacion)) # Se invoca la función de math que resolverá la operación.
        entrada1.set(f"√{operacion}")           # Se setea la entrada1 con la expresión de la operación.  
        entrada2.set(resultado)                 # Se setea la entrada2 con el resultado de la operación.
    except ValueError:
        entrada2.set("Error")                   # Nos devuelve un error si la función no se puede resolver.

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



# CONFIGURACIÓN DE LA VENTANA RAÍZ:
root = Tk()                           # Inicializa la ventana.  
root.title("Calculadora científica")  # Título.
root.geometry("+500+80")              # Tamaño. 
root.columnconfigure(0, weight=1)     # Posición en la pantalla.
root.rowconfigure(0, weight=1)        # Peso de la unica fila y columna de la ventana (proporción autoAjustable).


# CONFIGURAMOS EL ESTILO DE LA VENTANA:
estilos = ttk.Style()                                         # Función para dar estilos de ventana.  
estilos.theme_use("alt")                                      # Tema.
estilos.configure("mainframe.TFrame", background="#B2FCFF")   # Marco principal y BackGround. 
 
                                                            
# CREACIÓN DEL MARCO PRINCIPAL:
mainframe = ttk.Frame(root, style="mainframe.TFrame")    # Invocamos el marco. 
mainframe.grid(column=0, row=0, sticky=(W,N,E,S))        # Lo dibujamos con el método .grid 


# ASIGNACIÓN DE "COLUMNS" Y "ROWS" EN LA VENTANA RAIZ:
for i in range(6):                             # Utilizamos un bucle "for" para generar los índices de columnas.
    mainframe.columnconfigure(i, weight=1)     # "i" es el índice de la columna que se está configurando.
for i in range(8):                             # Generamos los índices de las filas. 
    mainframe.rowconfigure(i, weight=1)


# CREACIÓN DE WIDGETS "DISPLAYS":
estilos_label1 = ttk.Style()          # Utilizamos la funcion "Stiyle" para generarlo, y ".configure" para configurarlo.
estilos_label1.configure("Label1.TLabel", font="arial 15", anchor="e", background="#B2FCFF")

estilos_label2 = ttk.Style()
estilos_label2.configure("Label2.TLabel", font="arial 40", anchor="e", background="#B2FCFF")


# DECLARAMOS VARIABLES DE ENTRADAS:
# La variable StringVar vincula al widget con la entrada de datos.
# Con "ttk.Label" invocamos un widget dentro del marco principal, y asignamos los datos a la StringVar.
# Luego colocamos la etiqueta en la ventana. 
entrada1 = StringVar()             
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel") 
label_entrada1.grid(column=0, row=0, columnspan=6, sticky=(N, E, S, W))  

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=6, sticky=(N, E, S, W))

# Creamos otra variable StringVar para guardar el resultado.
resultadoAns = StringVar()



# CONFIGURAMOS EL ESTILO PARA LOS BOTONES NUMÉRICOS Y DE MANDO:
# La extensión "ttk" contiene funciones para diferentes estados,tipografpia, color de fondo, etc, del widget:
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("Botones_numero.TButton", font="arial 22", width=5, background="#51C3CC", relief="flat")
estilos_botones_numeros.map("Botones_numero.TButton", background=[("active", "#ADD8E6")]) 
                        
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
# Función "ttk.Button", generamos el botón, le asiganamos un valor, estylo, y comando:                                                                ...de clic del botón
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

# COMANDOS BÁSICOS:
# Utilizamos el valor "chr(9003)" para representar una flecha de retroceso.
boton_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
boton_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrarTodo())
boton_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: IngresarValores("("))
boton_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: IngresarValores(")"))
boton_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: IngresarValores("."))
boton_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: IngresarValores("="))

# COMANDOS ESPECIALES:
boton_ans = ttk.Button(mainframe, text="Ans", style="Botones_restantes.TButton", command=lambda: IngresarValores("Ans"))

# OPERACIONES BÁSICAS:
boton_division = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda: IngresarValores("/"))
boton_multi = ttk.Button(mainframe, text="x", style="Botones_restantes.TButton", command=lambda: IngresarValores("*"))
boton_suma = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: IngresarValores("+"))
boton_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: IngresarValores("-"))

# OPERACIONES ADICIONALES:
boton_porcentaje = ttk.Button(mainframe, text="%", style="Botones_restantes.TButton", command=lambda: porcentaje())
boton_raiz_cuadrada = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda: raizCuadrada())
boton_potencia = ttk.Button(mainframe, text="^", style="Botones_restantes.TButton", command=lambda: IngresarValores("**"))

# VALORES PRE-ESTABLECIDOS:
boton_pi = ttk.Button(mainframe, text="π", style="Botones_restantes.TButton", command=lambda: IngresarValores("π"))
boton_e = ttk.Button(mainframe, text="e", style="Botones_restantes.TButton", command=lambda: IngresarValores("e"))
boton_T = ttk.Button(mainframe, text="T", style="Botones_restantes.TButton", command=lambda: IngresarValores("T"))

# FUNCIONES TRIGONOMÉTRICAS:
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


# Configuramos ciertos parametros de diseño de los widgets hijos del widget padre (mainframe)
# Iniciamos un bucle que itera a través de todos los widgets hijos del marco principal
# mainframe.winfo_children() devuelve una lista que contiene todos los widgets hijos de mainframe
# child.grid_configure(ipady=10, padx=1, pady=1): Configuramos ciertos parámetros de diseño para cada widget hijo
# ipady=10: establece espacio vertical interno de 10 pixeles en los widgets
# padx=1:establece un espacio horizontal externo de 1 pixel entre los widgets
# pady=1: establece un espacio vertical externo de 1 pixel entre los widgets 
for child in mainframe.winfo_children(): 
    child.grid_configure(ipady=10, padx=2, pady=0.5)

# A traves de método "".bind" vinculamos el teclado a las funciones que cambian el color de pantalla.  
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