import json

info = """{
    "employee":[
        {
           "name":"Ivan",
           "salary":100000
        },
        {
           "name":"Vasily",
           "salary":110000
        },
        {
           "name":"Sergey",
           "salary":105000
        }
    ]
}"""

list_empl = json.loads(info)
print(list_empl)

for e in list_empl["employee"]:
    print(f"{e['name']} has {e['salary']}")