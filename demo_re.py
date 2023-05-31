# [а-яА-ЯёЁ] - кириллица
# [0-9]+ или \d+ - любые цифры
# [^0-9]+ или \D+ - всё кроме цифр
# [a-z0-9_]+ или \w
# \s - пробелы и табуляции

# Регулярные выражения - это язык напиания шаблона, которму должна соответствовать строка

from re import *

txt = """
    Ауди стоит 1000
    БМВ стоит 1200
    VW стоит 900
"""

# 1) Получим из текста список чисел. Пример с поиском

# numbers = findall("d+",txt) #получаем список чисел из строки
# print(numbers)

# 2) Замена через re
# rule = compile("\d+") #создали правило
# list = rule.findall(txt)
# print(list)
# print(rule.sub("...",txt)) #выполняем замену всех чисел на ...

# 3) Общие примеры
# text = "31 мая 2023 года"
# print(findall("\D+",text))
# print(int(findall("\d{4}",text)[0]))#получаем год в виде числа

# Проверка на email

# test@mail.ru

# rule = "^[a-zA-Z0-9_\.-]+@[a-zA-Z0-9_\.-]+\.[a-z]{2,5}$"
# rule = "^[\w\.-]+@[\w\.-]+\.[a-z]{2,5}$"
# if fullmatch(rule,"Test@bk.ru"):
#     print("Email корректный")
# else:
#     print("Емэйл некорректный")

# +7(9NN)NNN-NN-NN
