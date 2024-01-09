def f(x):
    x = str(x)
    most_in_raw = 1
    in_raw = 1
    print(len(x))
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            in_raw += 1
            if in_raw > most_in_raw:
                most_in_raw = in_raw
                number_rolled_most_1 = x[i]
        else:
            in_raw = 1
    return(number_rolled_most_1)
print(f(18311))