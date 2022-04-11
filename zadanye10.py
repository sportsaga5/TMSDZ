# задание 1 (создание калькулятора)
def division():   # деление
    try:
        first_value = int(input('Введите первое число: '))
        second_value = int(input('Введите второе число: '))
        result = first_value / second_value
        print(f'Результат деления: {result}')
    except ZeroDivisionError as error:
        print(error)
    except ValueError as error:
        print('Неверный тип данных!')

def multiplication():  # умножение
    try:
        first_value = int(input('Введите первое число: '))
        second_value = int(input('Введите второе число: '))
        result = first_value * second_value
        print(f'Результат умножения: {result}')
    except ValueError as error:
        print('Неверный тип данных!')

def summation():  # сложение
    try:
        first_value = int(input('Введите первое число: '))
        second_value = int(input('Введите второе число: '))
        result = first_value + second_value
        print(f'Результат сложения: {result}')
    except ValueError as error:
        print('Неверный тип данных!')

def subtraction():   # вычитание
    try:
        first_value = int(input('Введите первое число: '))
        second_value = int(input('Введите второе число: '))
        result = first_value - second_value
        print(f'Результат вычитания: {result}')
    except ValueError as error:
        print('Неверный тип данных!')

def calculate():
    action = input('Введите действие, которое хотите выполнить одним из 4 знаков (+ - / * ): ')
    if action == "+":
        summation()
    elif action == "-":
        subtraction()
    elif action == "/":
        division()
    elif action == "*":
        multiplication()
    else:
        print('Такое действие не поддерживается!')

calculate()