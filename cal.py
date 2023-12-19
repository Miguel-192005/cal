import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora")

        # Pantalla
        self.pantalla = tk.Entry(root, width=10, font=('Arial', 30), bg='white')  # Cambia bg='lightgray' es para cambiar el color deseado
        self.pantalla.grid(row=0, column=0, columnspan=4)

        # Botones
        self.crear_botones()

    def crear_botones(self):
        botones = [
            '1', '2', '3', '/',
            '4', '5', '6', '*',
            '7', '8', '9', '-',
            'C', '0', '=', '+'
        ]

        row, col = 1, 0
        for boton in botones:
            tk.Button(self.root, text=boton, width=5, height=2, command=lambda b=boton: self.click(b), bg='blue').grid(row=row, column=col)  # Cambia bg='gray' para el color deseado
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, valor):
        if valor == '=':
            try:
                resultado = str(eval(self.pantalla.get()))
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, resultado)
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error")
        elif valor == 'C':
            self.pantalla.delete(0, tk.END)
        else:
            self.pantalla.insert(tk.END, valor)

def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()

