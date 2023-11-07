sum = 0
mean = 0
Quantity = 0
while True:
    x = float(input('Enter number: '))
    sum += x
    if x == 0:
        print(f'RESULT: Quantity={Quantity}, Sum={sum}, Mean={mean}')
        break
    Quantity += 1
    if Quantity == 1:
        mean = x
    else:
        mean = sum / Quantity
    
