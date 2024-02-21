boton_pi.grid(column=5, row=4, sticky=(W, N, E, S))
boton_raiz_cuadrada.grid(column=3, row=7, sticky=(W,N,E,S))
= ttk.Button(mainframe, text="", style="Botones_funciones.TButton", command=lambda: ())
π
if tecla.isdigit() or tecla in "π":
            entrada2.set(entrada2.get() + tecla) 
def NumeroPi():
    try:
        resultado = math.pi()
        entrada1.set("π")
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")    
    #def numeroPi():            
    