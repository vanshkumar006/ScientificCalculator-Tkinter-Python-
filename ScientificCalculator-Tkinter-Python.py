import tkinter as tk
from tkinter import ttk
import math
import numpy as np

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("400x500")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Result display
        result_entry = ttk.Entry(self.master, textvariable=self.result_var, font=('Arial', 20), justify='right')
        result_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('π', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('exp', 5, 4),
            ('sqrt', 6, 0), ('x^2', 6, 1), ('x^y', 6, 2), ('1/x', 6, 3), ('abs', 6, 4)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(self.master, text=text, command=lambda x=text: self.button_click(x))
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

        # Configure grid weights
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)

    def button_click(self, key):
        if key == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif key == 'C':
            self.result_var.set("0")
        elif key == 'π':
            self.result_var.set(str(math.pi))
        elif key in ['sin', 'cos', 'tan', 'log', 'sqrt', 'abs']:
            try:
                num = float(self.result_var.get())
                if key == 'sin':
                    result = math.sin(num)
                elif key == 'cos':
                    result = math.cos(num)
                elif key == 'tan':
                    result = math.tan(num)
                elif key == 'log':
                    result = math.log10(num)
                elif key == 'sqrt':
                    result = math.sqrt(num)
                elif key == 'abs':
                    result = abs(num)
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif key == 'x^2':
            try:
                num = float(self.result_var.get())
                self.result_var.set(str(num ** 2))
            except:
                self.result_var.set("Error")
        elif key == 'x^y':
            self.result_var.set(self.result_var.get() + "**")
        elif key == '1/x':
            try:
                num = float(self.result_var.get())
                self.result_var.set(str(1 / num))
            except:
                self.result_var.set("Error")
        elif key == 'exp':
            self.result_var.set(str(math.e))
        else:
            if self.result_var.get() == "0":
                self.result_var.set(key)
            else:
                self.result_var.set(self.result_var.get() + key)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
