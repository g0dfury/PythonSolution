# easy 
import os
import shutil
# def is_exists(file_name: str()) -> bool:
#     try:
#         open(file_name, "r").close()
#     except FileNotFoundError:
#         return False
#     else:
#         return True

# while True:
#     file_name = input('Введите название файла: ')
#     if is_exists(file_name):
#         break
#     print(f"File \'{file_name}'\ does not exists, try again.")

# file = open(file_name, "r")
# for i in range(5):
#     print(file.readline())
# file.close()


# medium 
# filename = "ethics.txt"
# try:
#     file = open(filename, "r")
# except FileNotFoundError:
#         print("error")
# i = 1
# lines = file.readlines()
# for line in lines:
#     if i % 2 == 0:
#         print(line)
#     i += 1


# filename = "C:/Users/user/Desktop/python developer course/lesson_21/ethics.txt"
# try:
#     file = open(filename, "r")
# except FileNotFoundError:
#         print("error")
# i = 1
# lines = file.readlines()
# for line in lines:
#     if i % 2 != 0:
#         print(line)
#     i += 1

# file = open("ethics.txt", "r")
# lines = file.readlines()
# print('Odd elemets: ')
# print(*lines[0::2], sep=" ")
# print()
# print('Even elemets: ')
# print(*lines[1::2], sep=" ")
# file.close()


# hard
# open("new_ethics.txt", "x").close()
# ethics = open("ethics.txt", "r")
# new_ethics = open("new_ethics.txt", "w")

# for i in range(6):
#     line = ethics.readline()
#     new_ethics.write(line)
# ethics.close()
# new_ethics.close()

# for i in range(1,4):
#     shutil.copy("new_ethics.txt", f"new_ethics_copy{i}.txt")
#     os.mkdir(f"ethics{i}")
#     shutil.move(f"new_ethics_copy{i}.txt", f"ethics{i}")

# os.remove("new_ethics.txt")

