def is_it_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return(False)
            zet = False
        else:
            zet = True
    if x == 2:
        return(True)
    if zet:
        return(True)

number = int(input('Enter the number: '))
x = 2
y = 0
prime_numbers = []
while True:
    if is_it_prime(x):
        prime_numbers.append(x)
        y += 1
    x += 1
    if y == number:
        break
print('Prime numbers: ', str(prime_numbers)[1:-1])

