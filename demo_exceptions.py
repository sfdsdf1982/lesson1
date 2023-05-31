# Для обработки ошибок, которые появляются в момент запуска, можно
# обрабатывать с помощью оператор try/except
# Инструкции в которых возможны ошибки в момент запуска программы
# выносим в блок try. Как только возникает ошибка инртерпретор
# завершает выполнение инструкций в блоке try и переходит в блок
# except, в котором выполняем обработку ошибок

from random import randint
num1 = 10
num2 = randint(0,2)

# Первый пример
# try:
#     print(num1 / num2)
#     print("Если Вы видите этот текст, значит знаменатель при деление != 0")
# except ZeroDivisionError as e:
#     print("На 0 делить нельзя:",e.__doc__)

# Пример №2
# while True:
#     first_num = input("Введите первое число")
#     if first_num == 'q':
#         break
#     second_num = input("Введите первое число")
#     if second_num == 'q':
#         break
#     try:
#         res = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print("На 0 делить нельзя")
#     except ValueError:
#         print("Вы ввели некорректное значение")
#     except:
#         print("Возникла непредвиденная ошибка")
#     else: #Данный блок выполняется, если в try не было ошибки
#         print("Частное от деления:",res)\


# Пример №3

# my_file = 'text.txt'
# try:
#     file = open(my_file,"r")
#     content = file.readlines()
#     file.close()
# except FileNotFoundError:
#     print("Файл не найден")

# Пример №4
# Блок finally может находиться после try или except. Инструкции в блоке
#     finally запускаются в любом случае

# my_file = 'text.txt'
# file = None
# try:
#     file = open(my_file,"r")
#     content = file.readlines()
#     x = 2 / 0
# except Exception as s:
#     print(s.__doc__)
# finally:
#     print("Данный блок finally выполняется всегда")
#     if file != None:
#         file.close()
#         print("Файл закрыт")

# Пример №5

step = 0 #счетчик ошибочных вариантов ответа
while True:
    number = int(input("Введите целое число от 20 до 40\n"))
    if 20 <= number <= 40:
        print('Принимается')
        break
    else:
        step += 1
        if step == 3:
            raise Exception("Вы ввели некорректное значение 3 раза! Программа завершена")
        else:
            print("Вы опечатались! Попробуйте снова")

