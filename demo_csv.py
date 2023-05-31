import csv

persons = [
    ["Иван",80000],
    ["Олег",70000],
    ["Петр",90000],
]

# Запись данных в файл csv
with open('persons.csv','w',newline='') as file: #newline='', чтобы не было пустых строк
    obj = csv.writer(file,delimiter=':') #obj - переменная объект через который обращаемся к методам модуля
    obj.writerows(persons)

# with open('persons.csv','a',newline='') as file: #newline='', чтобы не было пустых строк
#     obj = csv.writer(file) #obj - переменная объект через который обращаемся к методам модуля
#     obj.writerow(['Анна',75000])

# Чтение данных из csv
# with open('persons.csv','r') as file:
#     obj = csv.reader(file)#объект для чтения данных
#     for line in obj: #line - это список, полученный на основе каждой строки файла
#         print(line[0],": ",line[1],sep="")

# Запись списка словарей в файл
cars = [
    {
        "title":"Audi",
        "price":1000,
        "color":"white"
    },
    {
        "title":"BMW",
        "price":1200,
        "color":"red"
    }
]

with open('cars.csv','w',newline='') as file: #newline='', чтобы не было пустых строк
    columns = ['title','price','color']
    obj = csv.DictWriter(file,fieldnames=columns) #obj - переменная объект через который обращаемся к методам модуля
    obj.writeheader()
    obj.writerows(cars)