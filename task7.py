from math import sqrt
a=[]
b=int(input())
for i in range(2, b+1):
    c=0
    for j in range(2, round(sqrt(i)+1)):
        if i%j==0:
            c+=1
            break
    if c==0:
        a.append(i)
print(a)
