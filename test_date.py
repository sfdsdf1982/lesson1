from datetime import *

now = datetime.today()
# print(now.strftime("%d.%m.%y"))

old_date = datetime(2022,12,31)

print(now.year)

print(now - old_date) #узнаем сколько прошло времени с нового года