import json

info = """{
    "cars":[
        {
           "id":1,
           "title":"Audi",
           "price":1000
        },
        {
           "id":2,
           "title":"BMW",
           "price":1200
        },
        {
           "id":3,
           "title":"VW",
           "price":900
        }
    ],
    "shop":{
        "title":"Элвис",
        "address":"Москва, Пионерская 13к5"
    }   
}"""

# Преобразование json в словарь
my_dict = json.loads(info) #получаем словарь
# print(my_dict)
# print(my_dict['cars'][1]['price'])
s = 0
for car in my_dict['cars']:
    print(f"Автомобиль {car['title']} стоит {car['price']}")
    s += car['price']
print("Сумма всех автомобилей:",s)
# print(my_dict['shop']['title'])

# Преобразование словаря в строку JSON
dict_to_json = json.dumps(my_dict,ensure_ascii=False)
print(dict_to_json)