from math import sqrt, pi, tan 
# # easy a 
a = int(input('a: ')) 
b = int(input('b: ')) 
print((sqrt(a)-sqrt(b))**2) 
 
# esay b 
 
a = int(input('a: ')) 
b = int(input('b: ')) 
result = -tan(a*pi/b) 
print(result) 
 
# medium a 
from random import randint 
from my_module import sum_of_digits 
random_number = randint(1000,9999) 
print(f'The sum of random number {random_number} is equal to {sum_of_digits(random_number)}') 
 
# medium b 
from my_module import my_sqrt, my_ceil, my_floor
print(f'sqrt of 121: {my_sqrt(121)}')
print(f'ceil of 4.7: {my_ceil(4.7)}')
print(f'floor of 4.7:{my_floor(4.7)}')


# hard a 
from random import choice 
my_list = [1, 2, 3, 4, 5, 6, 7, 8] 
counter = 0 
max_value = max(my_list) 
 
while True: 
    random_number = choice(my_list) 
    counter += 1 
    if random_number == max_value: 
        break 
 
print(f'# of attemts to get maximum value is {counter}')