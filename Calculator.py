from tkinter import Text, Button, Tk
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

        self.operations = {
            'sqrt': ('math.sqrt(', '√'),
            '^': ('**', '^'),
            'log': ('math.log10(', 'log('),
            'sin': ('math.sin(', 'sin('),
        }

        for val in [7, 8, 9, u"\u232B", 4, 5, 6, u"\u00f7", 1, 2, 3, '*', '.', 0, '+', '-', '=', 'sqrt', '^', 'log', 'sin']:
            self.createButton(val).grid(row=(val-1)//4 + 1, column=(val-1)%4)

    def createButton(self, val):
        if val in self.operations:
            return Button(self.master, text=self.operations[val][1], command=lambda: self.scientific(val),
                width=7, background="#4b7fa4", foreground="#fcfcec", font=("times", 20))
        elif val == u"\u232B":
            return Button(self.master, text=val, command=self.clear_screen,
                width=7, background="#4b7fa4", foreground="#fcfcec", font=("times", 20))
        elif val == '=':
            return Button(self.master, text=val, command=self.click,
                width=34, background="#4b7fa4", foreground="#fcfcec", font=("times", 20))
        else:
            return Button(self.master, text=val, command=lambda: self.insert_screen(val),
                width=7, background="#4b7fa4", foreground="#fcfcec", font=("times", 20))

    def click(self):
        try:
            answer = str(eval(self.equation.strip()))
        except ZeroDivisionError:
            answer = "Cannot divide by zero"
        except SyntaxError:
            answer = "Invalid expression"
        else:
            self.clear_screen()
            self.insert_screen(answer, newline=True)

    def scientific(self, operation):
        self.equation += self.operations[operation][0]
        self.insert_screen(self.operations[operation][1], False)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, '{}'.format(value))
        if newline:
            self.equation += '\n'
        else:
            self.equation += str(value)
        self.screen.configure(state='disable')

root = Tk()
my_gui = Calculator(root)
root.mainloop()
