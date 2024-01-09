def f(expresstion):
    x = 0
    while x <= len(expresstion):
        if x == 0:
            if expresstion[x+1] == '+':
                wynik = int(expresstion[x]) + int(expresstion[x+2])
            elif expresstion[x+1] == '-':
                wynik = int(expresstion[x]) + int(expresstion[x+2])
            x += 4
        else:
            if expresstion[x-1] == '+':
                wynik = wynik + int(expresstion[x])
            elif expresstion[x-1] == '-':
                wynik = wynik - int(expresstion[x])
            x += 2
    return(wynik)
print(f('2+3-4+5-0'))
