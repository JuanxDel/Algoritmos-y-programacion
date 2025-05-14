i=1
j=7
for x in range(10):
    while j!=0 and i<10:
        print(f"I={i} J={j}")
        j=j-1
        if j==4:
            i=i+2
            j=7