import re


email = input('Введите email:')
email_split = re.split(r"@", email)  # разделение email на 2 части
username = email_split[0]
hostname = email_split[1]

def username_check(username: str)-> bool: # проверка первой части 
    length_username = len(username)
    first_part = True
    if (username[0] == '.' or username[length_username-1] == '.'):
        first_part = False
    return first_part

def hostname_check(hostname: str)-> bool:   # проверка второй части 
    length_hostname = len(hostname)
    second_part = True
    if (hostname[0] == '-' or hostname[length_hostname-1] == '-'):
        second_part = False
    return second_part 

def email_check(email: str, first_part: str, second_part: str):
    email_regex = r'^([a-zA-Z0-9#%&*+-/=?^._`{|}~]+[!~]{0,1})+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{,63}$'
    if re.fullmatch(email_regex, email):
        if (first_part == True and second_part == True):
            return f'Email подходит'
        else:
            return f'Email не подходит'
    else:
        return f'Email не подходит'


first_check = username_check(username)
second_check = hostname_check(hostname)
print(email_check(email, first_check, second_check))