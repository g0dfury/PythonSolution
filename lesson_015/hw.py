# easy a
def degree(num: int|float, degree_of_num: int) -> int|float:
    return pow(num, degree_of_num)

def power(num: int|float, p:int) -> int|float:
    res = 1
    for i in range (p):
        res*=num
    return res
    

# easy b
def is_year_leap(year: int) -> bool:
    if year % 4 == 0:
        return True
    return False
    if year % 100 == 0:
        return True
    return False
    if year % 400 != 0:
        return True
    return False
print(is_year_leap(2012))


# medium a
def nod(a: int, b: int) -> int:
    
    while True:
        reminder = b % a
        if reminder == 0:
            return a
        b = a
        a = reminder

 
        

# medium b
def mean(my_list: list) -> float|int:
    result = sum(my_list) / len(my_list)
    return result

# for el in my_list:
#     summa += el
#     cnt += 1

#     return summa / cnt


print(mean([30, 63, 67, 29, 54, 30, 29, 41, 0]))
print(mean([3, 2, 6, 0]))

# hard a
def sum_of_digits(num: int) -> int|float:
    counter = 0
    while num > 0:
        counter += num % 10
        num //=10
    return counter


def sort_of_sum(some_list: list) -> list:
    return sorted(some_list, key=sum_of_digits)


# hard b
def string_reverse(text:str) -> str:
    words = text.split()
    return " ".join(words[::-1])

print(string_reverse('Каждый охотник желает знать, где сидит фазан.'))


# hard b v2.0   
def str_reverse():
    return " ".join(text.split()[::-1])


