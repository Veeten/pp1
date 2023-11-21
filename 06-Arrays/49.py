numbers = []
while True:
    try:
        rows = int(input('entner rows: '))
        columns = int(input('enter collumns: '))
        rows +=1
        break
    except:
        print('enter whole numbers')

for i in range(rows):
    numbers.append([])
    z = i
    for x in range(1,(columns+1)):
        numbers[i].append(i*x)

del numbers[0]
print(numbers)
