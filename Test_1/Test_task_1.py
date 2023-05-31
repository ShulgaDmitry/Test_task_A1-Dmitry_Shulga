#Представлен список из значений "Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13",
# "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro". Необходимо создать новый список,
# содержащий модели бренда Apple

mobile_list = [
    "Xiaomi Redmi Note 10S",
    "Смартфон Xiaomi Redmi Note 10 Pro",
    "Apple iPhone 13",
    "Apple iPhone 11",
    "Huawei nova Y70",
    "Смартфон Apple iPhone 13 Pro"
]
iphone_list = []
for phone in mobile_list:
    if phone.find("Apple") >= 0:
        iphone_list.append(phone)
print(iphone_list)
