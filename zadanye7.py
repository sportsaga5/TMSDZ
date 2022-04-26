import json
import csv
import re

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

users_file = 'users.txt'

def validate_credentials(func):
    def wrapper(email, password):

        password_rgx = r'[A-Za-z0-9@#$%^&+=]{8,}'
        if not re.fullmatch(password_rgx, password):
            raise Exception('Invalid password')

        email_rgx = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_rgx, email):
            raise Exception('Invalid email')

        func(email, password)
    return wrapper

        


def login(email: str, password: str):
    with open(users_file, 'r') as f:
        credentials = f'{email}:{password}'
        if credentials in f.read():
            print('Logged in')
        else:
            print('Invalid login or password')


@validate_credentials
def registration(email: str, password: str):
    with open(users_file, "a") as f:
        credentials = f'{email}:{password}\n'
        f.writelines([credentials])


def log_or_reg():
    x = input("Напишите 1 для авторизации или 2 для регистрации:")
    if x == "2":
        email = input("Введите email: ")
        password = input("Введите пароль: ")
        registration(email, password)        
    elif x == "1":
        email = input("Введите email: ")
        password = input("Введите пароль: ")
        login(email, password)
    else:
        print("Недопустимое значение, попробуйте снова!")


log_or_reg()