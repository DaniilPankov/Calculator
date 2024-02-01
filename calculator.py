class Calculator:

    def calc_sum(self, a: float, b: float) -> float:
        return a + b

    def calc_sub(self, a: float, b: float) -> float:
        return a - b

    def calc_mul(self, a: float, b: float) -> float:
        return a * b

    def calc_div(self, a: float, b: float) -> float:
        if abs(b) < 10 ** -8:
            raise ZeroDivisionError
        return a / b
