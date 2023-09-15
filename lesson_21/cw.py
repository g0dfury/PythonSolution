# work w files

# MODE "x"  ( если такого файла нет, он создается, либо скажет что такой файл уже существует)
try:
    file = open("abs.java", "x")
except FileExistsError:
    print('File already existed')   
else:
    file.close()
    print('File has been created')  # после создания

######### open исползует не стандартную кодировку (UTF-8), поэтому не читает кирилиццу
######### через encoding меняет кодировку для чтения кириллицы 


# MODE "r"  |   чтение (есть проблема, если файла не сущ, он сломается поэтому нужно try)
file = open("../python developer course/lesson_21/db.txt", "r", encoding='UTF-8')   
print(file.read())
print(file.readline())
print(file.readlines())
file.close()

# method    .read()  | читает все одной строкой
# method    .readline() | читает по одной линии, каждый следующий readline будет читать следующую строчку   
# method    .readlines() | читает все линии, создавая массив (считывает даже enter как \n)


# file = open("C:/Users/user/Desktop/portfolio/3214.png", "rb")     'rb' - для того что не читается текстом (гиф, видео, фото и тд.)
# print(file.read())                                                                


# MODE "w"  |   перезапись (удаляет все, чтоб перезаписать файл)
file = open("C:/Users/user/Desktop/python developer course/lesson_21/db.txt", "w")
file.write("c++\n")  # добавляет текст в конце
file.close()



# MODE "a"  |   дозапись (в случае отсутствия файла просто создаст его)
file = open("C:/Users/user/Desktop/python developer course/lesson_21/db.txt", "a")
file.write("c++\n")  # добавляет текст в конце
file.close()


# библиотеки
import os
import shutil
# os.mkdir("new_folder")    для создания папки
# os.rmdir("new_folder")    для удаления папки ( только пустой папки )
# shutil.rmtree("new_folder")   для удаления папки ( не важно пуста/непуста )
# os.remove("db.txt")   для удаления файлов
# os.rename("db.txt", "data_base.txt") для переименования файлов/папок
# shutil.copy("db.txt", "db_copy.txt")  для создания копии файла
# shutil.copytree("new_folder", "new_folder_copy")  для копии папки
# shutil.move("db.txt", "new_folder")   для перемещния файла


# 1) Относительный путь
file = open("../python developer course/lesson_21/db.txt", "r", encoding='UTF-8')   #ищем относительно текущего расположения
print(file.read())
file.close()

# 2) Абсолютный путь
file = open("C:/Users/user/Desktop/python developer course/for 21st lesson.txt", encoding="utf-8")    #ищем с самого начала (диск с)
print(file.read())
file.close()

