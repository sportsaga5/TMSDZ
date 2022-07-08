# задание 1 (создание геометрической прогрессии)
def geometry_progress():
    try:
        let = int(input('Введите число которое будет возводиться в степень: '))
        multiplier = int(input('Введите степень с которой будет идти прогрессия: '))
    except ValueError:
        print('Неверный тип данных!')
    while True:
        yield let
        let *= multiplier


try_to = geometry_progress()
try:
    x = int(input('Введите длину прогрессии: '))
except ValueError:
        print('Неверный тип данных!')

while x > 0:
    x -= 1
    print(next(try_to))