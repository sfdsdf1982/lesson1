from re import *

#
# rule = "^\+7\(9\d{2}\)\d{3}-\d{2}-\d{2}$"
rule = "^\+7\(9\d{2}\)\d{3}(-\d{2}){2}$"

if fullmatch(rule,"+7(923)111-11-11"):
    print("Номер корректный")
else:
    print("Номер некорректный")