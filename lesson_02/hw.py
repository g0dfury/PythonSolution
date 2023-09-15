# PROBLEM A (EASY)
# print ("Happy new " + str(2022))


# PROBLEM B (EASY)
# num1 = 5
# num2 = 6
# num3 = "2"
# print (num1+num2+int(num3))

#PROBLEM A MEDIUM
# print (2+3+6)
# print (-5+180+(-17))

#PROBLEM B MEDIUM
# формула 0.5 * а * б
# print (0.5*3*5)
# print (0.5*179*1534)

# PROBLEM A (HARD)
# num = int(input("Введите число: "))
# print (num % 10)



number = int(input("Введите число: "))
first = number // 100
middle = (number // 100) // 10
last = number % 10

print (first + middle + last)


