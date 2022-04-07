import json
import csv

# задание 1
def json_fail():
    """Добавляет имя и возраст в файл json"""
    with open("data_file.json", "w") as json_file:
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        credentials = f'{name}:{age}'
        json_file.write(credentials)
def csv_fail():
    """Добавляет имя и возраст в файл csv"""
    with open("data_file.csv", "w") as csv_file:
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        credentials = f'{name}:{age}'
        csv_file.write(credentials)

json_fail()
csv_fail()

# задание 2 
def log_or_reg():
    x = input("Напишите log для авторизации или reg для регистрации:")
    if x == "reg":
        with open("reg_file.csv", "a", newline = '') as f:
            login = input("Введите email:")
            password = input("Введите пароль:")
            data = [login, password]
            writer = csv.writer(f)
            writer.writerow(data)                
    elif x == "log":
        with open("reg_file.json") as write_fail:
            user_fail = json.dumps(write_fail.read())
            login = input("Введите email:")
            password = input("Введите пароль:")
            txt = f'{login}:{password}'
            for i in user_fail:
                if txt == i:
                    print("Авторизация прошла успешно")
                else:
                    print("Неправильное имя пользователя или пароль!")
    else:
        print("Недопустимое значение, попробуйте снова!")
        

log_or_reg()