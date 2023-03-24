from tkinter import *

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
            self.createButton('-'), self.createButton('=', None, 34)
        ]

        count = 0
        for row in range(1, 5):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count += 1
        buttons[16].grid(row=5, column=0, columnspan=4)

    def createButton(self, val, write=True, width=7):
        return Button(self.master, text=val, command=lambda: self.click(val, write),
            width=width, background="#4b7fa4", foreground="#fcfcec", font=("times", 20))

    def click(self, text, write):
        if write == None:
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

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        self.equation += str(value)
        if newline:
            self.equation += '\n'
        self.screen.configure(state='disable')

root = Tk()
my_gui = Calculator(root)
root.mainloop()