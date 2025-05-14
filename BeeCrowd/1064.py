n=[]
for i in range(6):
    f=float(input())
    if f>=0:
        n.append(f)
print(len(n),"valores positivos")
s=sum(n)
p=s/len(n)
print(f"{p:.1f}")