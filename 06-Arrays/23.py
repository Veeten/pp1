import random

array = []
for x in range(1000000):
    array.append(random.randrange(-10000, 10001))

x = 0
for i in array:
    if x == 0:
        min = i
        max = i
        x = 1
    if i > max:
        max = i 
    elif i < min:
        min = i

print(f'min = {min} max = {max}')