import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.config(bg="#000000")

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font=("Helvetica", 32), bd=0, insertwidth=4, width=14, borderwidth=0, bg="#000000", fg="#FFFFFF", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        buttons = [
            'C', '√', '(', ')',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '←'  # Backspace button
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            btn = tk.Button(self.root, text=button, padx=20, pady=20, font=("Helvetica", 24), bg="#1C1C1C", fg="white", activebackground="#3C3C3C", command=lambda b=button: self.on_button_click(b))
            btn.grid(row=row_val, column=col_val, sticky="nsew", ipadx=10)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif char == '√':
            try:
                self.expression = str(math.sqrt(float(self.expression)))
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1]  # Remove last character
        else:
            self.expression += str(char)

        self.update_display()

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
