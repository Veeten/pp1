names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
x = 0
for i in names:
    if int(len(i)) > x:
        x = len(i)
        longest_name = i

print(longest_name)