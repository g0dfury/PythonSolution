# easy 
class University:
    def __init__(self, off_name, location):
        self.off_name = off_name
        self.location = location
        
    def show_info_about_university(self):
        print(f"Name of university: {self.off_name}")
        print(f"Location: {self.location}") 
        print()

class Student(University):
    def __init__(self, off_name, location, full_name, specialty):
        super().__init__(off_name, location)
        self.full_name = full_name
        self.specialty = specialty

    def show_info_about_student(self):
        print(f"Name of student: {self.full_name}")
        print(f"Specialty of student: {self.specialty}")
        print(f"University: {self.off_name}")
        print()

class Professor(University):
    def __init__(self, off_name, location, full_name, subject):
        super().__init__(off_name, location)
        self.full_name = full_name
        self.subject = subject

    def show_info_about_professor(self):
        print(f"Name of professor: {self.full_name}")
        print(f"Subject of professor: {self.subject}")
        print(f"University: {self.off_name}")
        print()


university1 = University("SDU", "Kaskelen")
university2 = University("KBTU", "Tole-Bi street")
university3 = University("Kimep", "Abay street")

student1 = Student("SDU", "Kaskelen", "Garayev Emir", "Digital Marketing")
student2 = Student("KBTU", "Tole-Bi street", "Esmoldin Nazar", "Audit")
student3 = Student("Kimep", "Abay street", "Valerya Khan", "Marketing")

professor1 = Professor("SDU", "Kaskelen", "Firuza Osmamova", "Financial Accounting")
professor2 = Professor("KBTU", "Tole-Bi street", "Aigerim Tursynbekova", "Data Science")
professor3 = Professor("Kimep", "Abay street", "Bakhtier Meraliev", "Python")

for universities in [university1, university2, university3]:
    universities.show_info_about_university()

for students in [student1, student2, student3]:
    students.show_info_about_student()

for professors in [professor1, professor2, professor3]:
    professors.show_info_about_professor()




# # medium 
class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

class DeskTable(Table):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)
        
    def get_square(self):
        return self.length * self.width

desk = DeskTable(0.8, 0.6, 0.7)
res = desk.get_square()
print(res)
print()


# hard
class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

class DeskTable(Table):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)

    def get_square(self):
        return self.length * self.width

class ComputerTable(DeskTable):
    def __init__(self, length, width, height, monitor_area):
        super().__init__(length, width, height)
        self.monitor_area = monitor_area

    def working_place(self):
        return self.get_square() - self.monitor_area

desk = ComputerTable(0.8, 0.6, 0.7, 0.3)
ct = desk.working_place()
print(ct)