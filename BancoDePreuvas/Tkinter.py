import math
import tkinter as tk

class Calculator:
    def _init_(self, master):
        self.master = master
        master.title("Calculadora Científica")

        # Crear pantalla
        self.screen = tk.Entry(master, width=40, borderwidth=5)
        self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Crear botones
        self.create_button("(", 1, 0)
        self.create_button(")", 1, 1)
        self.create_button("π", 1, 2)
        self.create_button("e", 1, 3)
        self.create_button("sin", 2, 0)
        self.create_button("cos", 2, 1)
        self.create_button("tan", 2, 2)
        self.create_button("log", 2, 3)
        self.create_button("√", 3, 0)
        self.create_button("x²", 3, 1)
        self.create_button("x³", 3, 2)
        self.create_button("xⁿ", 3, 3)
        self.create_button("7", 4, 0)
        self.create_button("8", 4, 1)
        self.create_button("9", 4, 2)
        self.create_button("/", 4, 3)
        self.create_button("4", 5, 0)
        self.create_button("5", 5, 1)
        self.create_button("6", 5, 2)
        self.create_button("*", 5, 3)
        self.create_button("1", 6, 0)
        self.create_button("2", 6, 1)
        self.create_button("3", 6, 2)
        self.create_button("-", 6, 3)
        self.create_button("0", 7, 0)
        self.create_button(".", 7, 1)
        self.create_button("=", 7, 2)
        self.create_button("+", 7, 3)

        # Crear botón de borrar
        self.create_button("Borrar", 8, 0, columnspan=2)
        # Crear botón de salir
        self.create_button("Salir", 8, 2, columnspan=2)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, padx=40, pady=20, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan)

    def button_click(self, text):
        if text == "Borrar":
            self.screen.delete(0, tk.END)
        elif text == "Salir":
            self.master.quit()
        elif text == "=":
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, tk.END)
                self.screen.insert(0, result)
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        else:
            self.screen.insert(tk.END, text)

root = tk.Tk()
my_calculator = Calculator()
root.mainloop()