# Реализовать в Python цикл с постусловием.
y = 5

while True:

    print(y)

    if not y > 10:
        break

# Поменяться строковыми значениями (запрещено использовать/определять новые переменные):
x = "World"
y = "Hello "

y, x = x, y

# Должен получиться ответ: Hello World
print(x + y)

# (Для тех кто хочет посложнее) Почему выводится true:
x = 0.1 + 0.1 + 0.1

# Двоичное округление
print(x != 0.3)