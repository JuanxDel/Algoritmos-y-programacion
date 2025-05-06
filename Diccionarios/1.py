l = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
d = {}

for i in l:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1

print(d)
