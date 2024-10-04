from pprint import pprint
from tkinter.font import names


# «R»-это чтение от слова «read»,
# «w»-это «write» от слова записать, запись и
# «а»-это «append» добавление

# name = "Module_7_1\sample2.txt"
# file = open(name, 'r')
# print(file.tell())
# pprint(file.read())
# print(file.seek(15))
# pprint(file.read())
# file.close()


class Product:
    def __init__(self, name, weight, category):
        self.name = name    # название продукта (строка).
        self.weight = weight    #общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.category = category    #категория товара (строка).

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    # __file_name = 'products.txt'
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        # name = file1.txt
        file = open(self.__file_name, 'r')
        s = file.read()
        file.close()
        return s

    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in current_products:
                file.write(str(product) + '\n')
                current_products += str(product) + '\n'
                file.close()
            else:
                print(f'Продукт {self.name} уже есть в магазине.')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

