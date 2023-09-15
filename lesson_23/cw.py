# Class Legacy

# class Car:    
#     def turn_on(self):
#         print("Машина заведена.")

# class ElectroCar(Car):
    
#     charge = 90

#     def turn_on(self):
#         super().turn_on()   # обращается к методу turn_on родительского класса
#         print(f"Машина запустилась. Уровень заряда: {self.charge}%")

# tesla = ElectroCar()
# tesla.turn_on()



class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Human):
    def __init__(self, name, surname, age, course, gpa):
        super().__init__(name, surname, age)    # передали 3 аттрибута родительского класса
        self.course = course    # создание аттрибутов в дочернем классе
        self.gpa = gpa

    def information_about_student(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"GPA: {self.gpa}")

student1 = Student("Emir", "Garayev", 19, 2, 2.8)
student2 = Student("Dasha", "Shivtsova", 20, 2, 3.3)
student3 = Student("Inkgar", "Zhetpisbay", 19, 2, 4.0)

for students in [student1, student2, student3]:
    students.information_about_student()
    print()



