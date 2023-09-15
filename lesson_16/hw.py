def number_reverse(num: int, reversed_num: int = 0) -> int:
    if num == 0:
        return reversed_num
    else:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10
        return number_reverse(num, reversed_num)



# 5 ** 5 = (5**4) * 5
# 5 ** 4 = (5**3) * 5
# 5 ** 3 = (5**2) * 5
# 5 ** 2 = (5**1) * 5 
# 5 ** 1 = (5**0) * 5

def degree_rec(number: int, degree: int):
    if degree == 0:
        return 1
    elif degree == 1:
        return number
    else:
        return degree_rec(number, degree-1) * number


def monotone_sequences(size: int, i = 1, counter = 0) -> None:
    if number == 0:
        return 0
    if counter < i:
        print(i, end=' ')
        monotone_sequences(size - 1, i, counter + 1)
    elif counter == i:
        monotone_sequences(size, i + 1, 0)





