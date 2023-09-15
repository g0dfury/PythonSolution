# # # class / классы
# # Классы можно импортировать в других файлах

# # Пример 1

# # class Human:
# #     name = "Emir"       # attribute name
# #     age = 19            # attribute age

# # human1 = Human()
# # print(human1.name, human1,age)
# human2 = Human('Emir', 19) # error (класс не принимает аттрибуты)
# print(human2)


# # Пример 2

# class Human:

#     #self - универсальный объект, обращение к аттрибутам 

#     def __init__(self, name: str, age: int):         #constructor
#         self.name = name
#         self.age = age
#         self.salary = 0
#         self.cars = ['toyota', 'bmw']
    
#     def grading(self, salary_uppdate: int|float):     # метод grading
#         self.salary += salary_uppdate
  
# #     def bd(self):
# #         self.age += 1



# human1 = Human("Emir", 19)
# # human2 = Human("Zhenya", 19)

# print(human1.salary)
# human1.grading(200_000)
# human1.grading(10_000)
# print(human1.salary)

# # print(human1.name)
# # print(human1.age)
# # print(human2.name)
# # print(human2.age)


# n = 5
# if type(n) == int:
#     print('yes')

# if isinstance(n, int):
#     print('yes')

# print(type(human2) == Human)
# print(isinstance(human2, Human))





# # class work
# class Person:
#     # name = "Emir"
#     # age = "19 years old"    # аргумент
#     # height = "175 sm"
    
#     def __init__(self, name, age):  # конструктор
#         self.name = name        #создание аттрибута age и присовние ему данных
#         self.age = age  
#         self.height = 173     # не обязательно передавать аттрибут в конструктор если он имеет дефолтное неизменчивое значение 
#         self.cars = [] 

#     def car_purchasing(self, automobile: str):
#         self.cars.append(automobile)

#     def bd(self):
#         self.age += 1



# cw

# from math import sqrt

# class Point:
#     def __init__(self, x2, x1, y2, y1):
#         self.x2 = x2
#         self.x1 = x1
#         self.y2 = y2
#         self.y1 = y1

#     def dist(self):
#          return sqrt((self.x2-self.x1)**2 + (self.y2 - self.y1)**2)
# x2 = int(input())
# x1 = int(input())
# y2 = int(input())
# y1 = int(input())
# point_object = Point(x2, x1, y2, y1)    # class object
# print(point_object.dist())
        


# class Rect:
#     def __init__(self, length: int|float, width: int|float) -> bool:
#         self.length = length
#         self.width = width

#     def is_square(self):
#         if self.length == self.width:
#             return True
#         return False

# # Object creating
# length = int(input())
# width = int(input())
# rects_object = Rect(length, width)

# print(rects_object.is_square())



class Shop:         # создал класс
    def __init__(self, products: dict = {}):     # опицональный параметр, нам передают products, а если нет мы возвращаем пустой словарь
        self.products = products
        self.basket = {}

        def add_to_basket(self, product_name: str):   # метод
            if product_name not in self.products:
                print(f"We do not have any {product_name}.")
                print()
                return
            if product_name in self.basket.keys():
                self.basket[product_name] += 1
            else:
                self.basket[product_name] = 1
                print(f"{product_name} has been added to your basket.")
                print()

        def remove_from_basket(self, product_name: str):
            if product_name not in self.products.keys():
                print(f"We do not have any {product_name}.")
                print()
                return
            if product_name in self.basket.keys():
                self.basket[product_name] -= 1
                print(f"{product_name} has been deleted from your basket.")
                print()
            else:
                print(f"You do not have {product_name} in your basket.")
                print()

        def show_products(self):
            if self.products:
                print("Your product list: ")
                for prd_name, prd_quant in self.basket.items():
                    print(f"name: {prd_name}, quantity: {prd_quant}, price: {prd_quant * self.products[prd_name]}$.")
                    print()
            else:
                print("basket is empty")

        def total_price(self):
            total = 0
            for prd_name, prd_quant in self.basket.items():
                total += prd_cnt * self.products[prd_name]
            return total
        
        def average_price(self):
            return self.total_price() / sum(self.basket.values())


shop = Shop({
    "bread": 2.0,
    "milk": 2.5,
    "juice": 4.0,
    "fruits": 3.5
})

shop.add_to_basket("elfbar")