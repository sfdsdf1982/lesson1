import xml.etree.ElementTree as parser

# Получаем содержимое xml документа в виде объекта
tree = parser.parse('store.xml') #объект tree получает информацию о всей структуре нашего документа

root = tree.getroot() #root - корневой элемент документа
# print(root.tag)

for item in root:
    print(item.tag,': ',item.text,sep="")
    for i in item: #обходим каждый вложенный тэг
        print(i.tag,': ',i.text,sep="")
