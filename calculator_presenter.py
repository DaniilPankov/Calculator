from calculator import Calculator
from calculator_view import CalculatorView


class CalculatorPresenter:
    def __init__(self):
        self.calc_view = CalculatorView()
        self.calc_view.set_sum_btn_command(self.on_plus_clicked)
        self.calc_view.set_sub_btn_command(self.on_minus_clicked)
        self.calc_view.set_mul_btn_command(self.on_multiply_clicked)
        self.calc_view.set_div_btn_command(self.on_divide_clicked)
        self.calc = Calculator()

    def start(self):
        self.calc_view.start()

    def on_plus_clicked(self):
        try:
            first_argument = self.calc_view.get_first_argument()
            second_argument = self.calc_view.get_second_argument()
            result = self.calc.calc_sum(first_argument, second_argument)
            self.calc_view.print_result(result)
        except ValueError:
            self.calc_view.display_error("Поля нужно заполнить числами")

    def on_minus_clicked(self):
        try:
            first_argument = self.calc_view.get_first_argument()
            second_argument = self.calc_view.get_second_argument()
            result = self.calc.calc_sub(first_argument, second_argument)
            self.calc_view.print_result(result)
        except ValueError:
            self.calc_view.display_error("Поля нужно заполнить числами")

    def on_multiply_clicked(self):
        try:
            first_argument = self.calc_view.get_first_argument()
            second_argument = self.calc_view.get_second_argument()
            result = self.calc.calc_mul(first_argument, second_argument)
            self.calc_view.print_result(result)
        except ValueError:
            self.calc_view.display_error("Поля нужно заполнить числами")

    def on_divide_clicked(self):
        try:
            first_argument = self.calc_view.get_first_argument()
            second_argument = self.calc_view.get_second_argument()
            result = self.calc.calc_div(first_argument, second_argument)
            self.calc_view.print_result(result)
        except ValueError:
            self.calc_view.display_error("Поля нужно заполнить числами")
        except ZeroDivisionError:
            self.calc_view.display_error("На ноль делить нельзя")


if __name__ == "__main__":
    calculator = CalculatorPresenter()
    calculator.start()

