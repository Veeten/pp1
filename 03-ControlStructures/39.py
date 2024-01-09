lenght = int(input('lenght'))
height = int(input('height'))
for i in range(1, height):
    if i == 1 or i == (height - 1):
        print('*' * lenght)
    else:
        print('*' + (lenght - 2) * ' ' + '*')