def star(n):
    return (n * '*')

numbers = [12,6,4,9,10]
for i in numbers:
    if i < 10:
        print(' ', end='')
    print(f'{i}: ', star(i))