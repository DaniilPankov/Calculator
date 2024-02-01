import pytest
import random as rand
from calculator import Calculator
import unittest
from unittest.mock import MagicMock
from calculator_presenter import CalculatorPresenter


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        # Создаем фиктивные объекты Calculator И CalculatorView
        self.mock_calculator = MagicMock()
        self.mock_view = MagicMock()

        # Передаем фиктивные объекты в CalculatorPresenter
        self.presenter = CalculatorPresenter()
        self.presenter.calc = self.mock_calculator
        self.presenter.calc_view = self.mock_view

    def test_on_plus_clicked(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 2
        self.mock_view.get_second_argument.return_value = 3
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_sum.return_value = 5.0
        # Как бы нажимаем на "+"
        self.presenter.on_plus_clicked()
        # Проверяем, что был вызван метод calc_sum c нужными аргументами
        self.mock_calculator.calc_sum.assert_called_once_with(2.0, 3.0)
        # Проверяем, что был вызван метод print_result c правильным результатом
        self.mock_view.print_result.assert_called_once_with(5.0)

    def test_on_minus_clicked(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 5
        self.mock_view.get_second_argument.return_value = 3
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_sub.return_value = 2.0
        # Как бы нажимаем на "-"
        self.presenter.on_minus_clicked()
        # Проверяем, что был вызван метод calc_sum c нужными аргументами
        self.mock_calculator.calc_sub.assert_called_once_with(5.0, 3.0)
        # Проверяем, что был вызван метод print_result c правильным результатом
        self.mock_view.print_result.assert_called_once_with(2.0)

    def test_on_multiply_clicked(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 5
        self.mock_view.get_second_argument.return_value = 3
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_mul.return_value = 15.0
        # Как бы нажимаем на "*"
        self.presenter.on_multiply_clicked()
        # Проверяем, что был вызван метод calc_sum c нужными аргументами
        self.mock_calculator.calc_mul.assert_called_once_with(5.0, 3.0)
        # Проверяем, что был вызван метод print_result c правильным результатом
        self.mock_view.print_result.assert_called_once_with(15.0)

    def test_on_divide_clicked(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 5
        self.mock_view.get_second_argument.return_value = 1
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_div.return_value = 5.0
        # Как бы нажимаем на "/"
        self.presenter.on_divide_clicked()
        # Проверяем, что был вызван метод calc_sum c нужными аргументами
        self.mock_calculator.calc_div.assert_called_once_with(5.0, 1.0)
        # Проверяем, что был вызван метод print_result c правильным результатом
        self.mock_view.print_result.assert_called_once_with(5.0)

    def test_on_plus_clicked_None(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 2
        self.mock_view.get_second_argument.return_value = None
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_sum.side_effect = ValueError()
        # Как бы нажимаем на "+"
        self.presenter.on_plus_clicked()
        # Проверяем, что был вызван метод display_error c правильной ошибкой
        self.mock_view.display_error.assert_called_once_with("Поля нужно заполнить числами")

    def test_on_minus_clicked_None(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 5
        self.mock_view.get_second_argument.return_value = None
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_sub.side_effect = ValueError()
        # Как бы нажимаем на "-"
        self.presenter.on_minus_clicked()
        # Проверяем, что был вызван метод display_error c правильной ошибкой
        self.mock_view.display_error.assert_called_once_with("Поля нужно заполнить числами")

    def test_on_multiply_clicked_None(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 5
        self.mock_view.get_second_argument.return_value = None
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_mul.side_effect = ValueError()
        # Как бы нажимаем на "*"
        self.presenter.on_multiply_clicked()
        # Проверяем, что был вызван метод display_error c правильной ошибкой
        self.mock_view.display_error.assert_called_once_with("Поля нужно заполнить числами")


    def test_on_divide_clicked_None(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 5
        self.mock_view.get_second_argument.return_value = None
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_div.side_effect = ValueError()
        # Как бы нажимаем на "/"
        self.presenter.on_divide_clicked()
        # Проверяем, что был вызван метод display_error c правильной ошибкой
        self.mock_view.display_error.assert_called_once_with("Поля нужно заполнить числами")

    def test_on_divide_clicked_zero(self):
        # Устанавливаем первоначальные значение полей ввода
        self.mock_view.get_first_argument.return_value = 5
        self.mock_view.get_second_argument.return_value = 0
        # Заменяем реальные методы объекта Calculator на MagicMock
        self.mock_calculator.calc_div.side_effect = ZeroDivisionError()
        # Как бы нажимаем на "/"
        self.presenter.on_divide_clicked()
        # Проверяем, что был вызван метод display_error c правильной ошибкой
        self.mock_view.display_error.assert_called_once_with("На ноль делить нельзя")


    def test_first_argument_is_None_sum(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_sum(None, 10)

    def test_second_argument_is_None_sum(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_sum(10, None)

    def test_first_argument_is_None_sub(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_sub(None, 10)

    def test_second_argument_is_None_sub(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_sub(10, None)

    def test_first_argument_is_None_mul(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_mul(None, 10)

    def test_second_argument_is_None_mul(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_mul(10, None)

    def test_first_argument_is_None_div(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_div(None, 10)

    def test_second_argument_is_None_div(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_div(10, None)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calc_div(10, 0.6 * 10 ** -8)

    @pytest.mark.repeat(100)
    def test_sum(self):
        a = rand.random()
        b = rand.random()
        self.assertEqual(self.calculator.calc_sum(a, b), a + b)

    @pytest.mark.repeat(100)
    def test_sub(self):
        a = rand.random()
        b = rand.random()
        self.assertEqual(self.calculator.calc_sub(a, b), a - b)

    @pytest.mark.repeat(100)
    def test_mul(self):
        a = rand.random()
        b = rand.random()
        self.assertEqual(self.calculator.calc_mul(a, b), a * b)

    @pytest.mark.repeat(100)
    def test_dev(self):
        a = rand.random()
        b = rand.random()
        self.assertEqual(self.calculator.calc_div(a, b), a / b)



