import pymysql.cursors
from pprint import pprint
from pymysql import *

def show_goods(cur):
    cur.execute("select * from goods")
    rows = cur.fetchall()  # получаем все данные после запроса в виде списка словарей
    #pprint(rows)
    for item in rows:
        print(f"Автомобиль {item['title']} стоит {item['price']}")

def update(cur):
    info = input("Введите название товара и"
                 " для него новую стоимость, используйте пробел").split(" ")
    sql = f"UPDATE goods SET price = {int(info[1])} WHERE title = '{info[0]}'"
    if cur.execute(sql) > 0:
        print("Информация обновлена!")


connect = connect(host="localhost",
                  user="root",
                  password="root",
                  db="lesson003",
                  cursorclass=pymysql.cursors.DictCursor #для возможности работать с информацией из таблицы в виде словаря
                  )

with connect: #при успешном подключении к серверу базы данных
    cur = connect.cursor() #получили объект, с помощью которого можно выполнять любые sql запросы на сервере
    show_goods(cur)
    update(cur)
    connect.commit() #подтверждаем изменение в базе данных
    print("\nТовары после обновления цены\n")
    show_goods(cur)
