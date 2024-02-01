from tkinter import *


class CalculatorView:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("400x100")
        self.root.resizable(False, False)

        self.num_1_label = Label(text="Введите первое число:")
        self.num_1_label.place(x=10, y=10)

        self.num_1 = Entry(width=10, font="Times")
        self.num_1.place(x=140, y=10)

        self.num_1_label = Label(text="Введите второе число:")
        self.num_1_label.place(x=10, y=40)

        self.num_2 = Entry(width=10, font="Times")
        self.num_2.place(x=140, y=40)

        self.result_field = Label(text='Result: ')
        self.result_field.place(x=99, y=70)

        self.sum_btn = Button(text="+", width=1, height=1)
        self.sum_btn.place(x=230, y=10)

        self.sub_btn = Button(text="-", width=1, height=1)
        self.sub_btn.place(x=250, y=10)

        self.mul_btn = Button(text="*", width=1, height=1)
        self.mul_btn.place(x=230, y=40)

        self.div_btn = Button(text="/", width=1, height=1)
        self.div_btn.place(x=250, y=40)

    def start(self):
        self.root.mainloop()

    def print_result(self, result):
        self.result_field.configure(text=f"Result: {result}")

    def display_error(self, message):
        self.result_field.configure(text=f"Ошибка: {message}")

    def get_first_argument(self):
        return float(self.num_1.get())

    def get_second_argument(self):
        return float(self.num_2.get())

    def set_sum_btn_command(self, cmd):
        self.sum_btn.configure(command=cmd)

    def set_sub_btn_command(self, cmd):
        self.sub_btn.configure(command=cmd)

    def set_mul_btn_command(self, cmd):
        self.mul_btn.configure(command=cmd)

    def set_div_btn_command(self, cmd):
        self.div_btn.configure(command=cmd)
