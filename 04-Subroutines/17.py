def different(n1, n2, n3):
    return(bool(n1 == n2 == n3))

n1 = input('Enter first number: …')
n2 = input('Enter second number: …')
n3 = input('Enter third number: …')
    
if different(n1, n2, n3) == True:
    print(f'Numbers {n1}, {n2}, {n3}, are the same')
else:
    print(f'Numbers {n1}, {n2}, {n3}, are different')