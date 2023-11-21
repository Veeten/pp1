def create_2d_arr(x,y):
    d2_a = []
    for i in range(x):
        d2_a.append([])
        for x in range(y):
            d2_a[i].append(0)
    return d2_a

print(create_2d_arr(4,4))
