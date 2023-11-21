numbers = [[-38, 19], [5,40],[-7,11],[29,16]]
minimal = 0
maximal = 0
for i in numbers:
    if max(i) > maximal:
        maximal = max(i)
    if min(i) < minimal:
        minimal = min(i)

print(minimal, maximal)