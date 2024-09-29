a=[]
for i in range(100, 999):
    if (i%10)**3+((i%100-i%10)/10)**3+((i-i%100)/100)**3==i:
        a.append(i)
print(a)
