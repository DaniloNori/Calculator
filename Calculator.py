from tkinter import *
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")
        master.configure(bg='#cb464e')

        self.screen = Text(master, state='disable', width=60,
            height=3, background="#fcfcec", foreground="#cb464e", font=("times", 12, "bold"))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        self.equation = ''

        buttons = [
            self.createButton(7), self.createButton(8), self.createButton(9),
            self.createButton(u"\u232B", None), self.createButton(4), self.createButton(5),
            self.createButton(6), self.createButton(u"\u00f7"), self.createButton(1),
            self.createButton(2), self.createButton(3), self.createButton('*'),
            self.createButton('.'), self.createButton(0), self.createButton('+'),
            self.createButton('-'), self.createButton('=', None, 34),
            self.createButton('sqrt', False), self.createButton('^', False),
            self.createButton('log', False), self.createButton('sin', False),
        ]

        count = 0
        for row in range(1, 6):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count += 1

    def createButton(self, val, write=True, width=7):
        if write:
            return Button(self.master, text=val, command=lambda: self.click(val),
                width=width, background="#4b7fa4", foreground="#fcfcec", font=("times", 20))
        else:
            return Button(self.master, text=val, command=lambda: self.scientific(val),
                width=width, background="#4b7fa4", foreground="#fcfcec", font=("times", 20))

    def click(self, text):
        if text == '=' and self.equation:
            try:
                answer = str(eval(self.equation))
            except:
                answer = "Error"
            self.clear_screen()
            self.insert_screen(answer, newline=True)
        elif text == u"\u232B":
            self.clear_screen()
        else:
            self.insert_screen(text)

    def scientific(self, operation):
        if operation == 'sqrt':
            self.equation += 'math.sqrt('
            self.insert_screen('sqrt(', False)
        elif operation == '^':
            self.equation += '**'
            self.insert_screen('^', False)
        elif operation == 'log':
            self.equation += 'math.log10('
            self.insert_screen('log(', False)
        elif operation == 'sin':
            self.equation += 'math.sin('
            self.insert_screen('sin(', False)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        if newline:
            self.equation += '\n'
        else:
            self.equation += str(value)
        self.screen.configure(state='disable')

root = Tk()
my_gui = Calculator(root)
root.mainloop()