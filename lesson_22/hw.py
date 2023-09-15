# easy a
# class Almira:
#     def __init__(self, name, age):
#         if name != 'Almira':
#             self.name = 'Almira'
#         else:
#             self.name = name
#         self.age = age

# ob = Almira('Erlan', 22)
# print(ob.name, ob.age)



# md
# class Gazirovka:
#     def __init__(self, dobavka):
#         self.dobavka = dobavka
        
#     def show_my_drink(self):
#         if self.dobavka:
#             print(f"Газировка и {self.dobavka}")
#         else:
#             print("Обычная газировка")

# x = input()
# g1 = Gazirovka(x)
# g1.show_my_drink() 


# hard  
class Triangle:
    def is_it_triangle(self, a, b, c):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
            return "Нужно вводить только числа!"
        elif a <= 0 or b <= 0 or c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        elif a + b > c and a + c > b and b + c > a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

