import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for display
        entry = tk.Entry(self.root, font=('Arial', 20), textvariable=self.text_input, bd=10, insertwidth=2, width=14,
                         borderwidth=4, relief='ridge', justify='right', state='readonly', readonlybackground='white')
        entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for btn in buttons:
            if btn[0] == '=':
                b = tk.Button(self.root, text=btn[0], padx=90, pady=20, font=('Arial', 14, 'bold'),
                              command=self.equal_press, bg='#4CAF50', fg='white')
                b.grid(row=btn[1], column=btn[2], columnspan=btn[3], sticky="nsew")
            elif btn[0] == 'C':
                b = tk.Button(self.root, text=btn[0], padx=20, pady=20, font=('Arial', 14, 'bold'),
                              command=self.clear, bg='#f44336', fg='white')
                b.grid(row=btn[1], column=btn[2], sticky="nsew")
            else:
                b = tk.Button(self.root, text=btn[0], padx=20, pady=20, font=('Arial', 14, 'bold'),
                              command=lambda char=btn[0]: self.button_press(char))
                b.grid(row=btn[1], column=btn[2], sticky="nsew")

        # Configure grid weights for resizing
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def button_press(self, char):
        self.expression += str(char)
        self.text_input.set(self.expression)

    def clear(self):
        self.expression = ""
        self.text_input.set("")

    def equal_press(self):
        try:
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.expression = result
        except Exception:
            self.text_input.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
