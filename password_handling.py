# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.

import re
import bcrypt

user_password = input('Введите пароль: не менее 8 символов, обязательно наличие прописных, строчных букв и цифр: ')

pattern = "(?=.*\d)(?=.*[a-z | а-я])(?=.*[A-Z | А-Я]).{8,}"
result = re.search(pattern, user_password)
if result is not None:
    print('Хороший пароль! Держи хэш!')
    hashed_user_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
    print(hashed_user_password)
else:
    print('Нет, этот пароль не удовлетворяет условию выше!')
