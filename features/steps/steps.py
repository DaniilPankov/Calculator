import os.path
import sys
from behave import *

sys.path.insert(0, os.path.join(os.getcwd(), '..//..'))
from calculator_presenter import CalculatorPresenter


@given('I have a calculator')
def step_init(context):
    context.calc_pres = CalculatorPresenter()


@given('I have entered {a} in first entry')
def step_impl(context, a):
    context.calc_pres.calc_view.num_1.insert(0, a)

@step('I have entered {b} in second entry')
def step_impl(context, b):
    context.calc_pres.calc_view.num_2.insert(0, b)


@when('I press sum button')
def step_impl(context):
    context.calc_pres.on_plus_clicked()

@when('I press sub button')
def step_impl(context):
    context.calc_pres.on_minus_clicked()


@when('I press mul button')
def step_impl(context):
    context.calc_pres.on_multiply_clicked()


@when('I press div button')
def step_impl(context):
    context.calc_pres.on_divide_clicked()


@then('The result should be {res} on the screen')
def step_impl(context, res: int):
    assert (context.calc_pres.calc_view.result_field.cget("text") == f"Result: {res}")

@then('An error ZeroDivision should be raised')
def step_impl(context):
    assert (context.calc_pres.calc_view.result_field.cget("text") == "Ошибка: На ноль делить нельзя")

@then('An ValueError should be raised')
def step_impl(context):
    assert (context.calc_pres.calc_view.result_field.cget("text") == "Ошибка: Поля нужно заполнить числами")
