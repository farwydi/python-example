#!/usr/bin/env python
# coding: utf-8

import string


# На вход Вашей функции будет передано одно предложение.
# Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
# Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку,
# то добавлять еще одну не нужно, это будет ошибкой
#
# Входные аргументы: Строка (A string).
# Выходные аргументы: Строка (A string).
#
# Предусловия: В начале и конце нет пробелов, текст состоит только из пробелов, a-z A-Z , и .

# In[ ]:
def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here

    text = text.strip()
    text = text[0].upper() + text[1:]
    if text[-1] != ".":
        text += "."

    # end your code
    return text


# These "asserts" are used for self-checking and not for an auto-testing
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("      Greetings, friends") == "Greetings, friends."
assert correct_sentence("      greetings, friends       ") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("hi") == "Hi."
assert correct_sentence("welcome to New York") == "Welcome to New York."


# Вы должны написать функцию, которая представит человека по переданным параметрам.
#
# Входные данные: Два аргумента строка(str) и положительное число(int)
#
# Output: Строка(str).

# In[ ]:
def say_hi(name: str, age: int) -> str:
    """
        Hi!
    """
    # your code here
    return f"Hi. My name is {name} and I'm {age} years old"
    # end your code


# These "asserts" using only for self-checking and not necessary for auto-testing
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"


# Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
#
# Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims".
# Если бы нам надо было найти ее первое вхождение, то тут все просто: с помощью функции index или find мы можем узнать,
# что "s" – это самый первый символ в слове "sims",
# а значит индекс первого вхождения равен 0. Но нам необходимо найти вторую "s", а она 4-ая по счету.
# Значит индекс второго вхождения (и ответ на вопрос) равен 3.
#
# Input: Две строки (String).
#
# Output: Int or None

# In[2]:
def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    first = text.find(symbol)
    if first != -1:
        second = text.find(symbol, first + 1)
        if second != -1:
            return second
        return None

    return None
    # end your code


# These "asserts" are used for self-checking and not for an auto-testing
assert second_index("sims", "s") == 3, "First"
assert second_index("find the river", "e") == 12, "Second"
assert second_index("hi", " ") is None, "Third"
assert second_index("hi mayor", " ") is None, "Fourth"
assert second_index("hi mr Mayor", " ") == 5, "Fifth"


# Разработать модуль для проверки паролей на безопасность. Пароль считается достаточно стойким,
# если его длина больше или равна 10 символам,
# он содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре.
# Пароль может содержать только латинские буквы и/или цифры.
#
# Вх. данные: Пароль как строка.
#
# Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого типа данных,
# который может быть сконвертирован и представлен как булево значение (True или False)
#
# Предусловия:
# re.match("[a-zA-Z0-9]+", password)
# 0 < len(password) ≤ 64

# In[ ]:
def check(data: str) -> bool:
    # your code here
    if len(data) < 10:
        return False

    upper = False
    lower = False
    nummb = False

    for lt in data:
        if upper and lower and nummb:
            return True

        if not upper:
            upper = lt in string.ascii_uppercase
        if not lower:
            lower = lt in string.ascii_lowercase
        if not nummb:
            nummb = lt in string.digits

    # end your code
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
assert check('A1213pokl') == False, "1st example"
assert check('bAse730onE4') == True, "2nd example"
assert check('asasasasasasasaas') == False, "3rd example"
assert check('QWERTYqwerty') == False, "4th example"
assert check('123456123456') == False, "5th example"
assert check('QwErTy911poqqqq') == True, "6th example"
