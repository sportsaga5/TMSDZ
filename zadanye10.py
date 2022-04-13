# задание 1 (создание калькулятора)
def division(value: tuple) -> str:   # деление
    try:
        result = value[0] / value[1]
        print(f'Результат деления: {result}')
    except ZeroDivisionError as error:
        print(error)

def multiplication(value: tuple) -> str:  # умножение
    result = value[0] * value[1]
    print(f'Результат умножения: {result}')

def summation(value: tuple) -> str:  # сложение
    result = value[0] + value[1]
    print(f'Результат сложения: {result}')

def subtraction(value: tuple) -> str:  # вычитание
    result = value[0] - value[1]
    print(f'Результат вычитания: {result}')
    

def calculate():
    try:
        first_value = int(input('Введите первое число: '))
        second_value = int(input('Введите второе число: '))
        value = (first_value, second_value)
        action = input('Введите действие, которое хотите выполнить одним из 4 знаков (+ - / * ): ')
        if action == "+":
            summation(value)
        elif action == "-":
            subtraction(value)
        elif action == "/":
            division(value)
        elif action == "*":
            multiplication(value)
        else:
            print('Такое действие не поддерживается!')
    except ValueError:
        print('Неверный тип данных!')

calculate()