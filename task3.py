print("Напишите возраст")
a=int(input())
if a%10==1 and (a%100<5 or a%100>20):
    print(a, "год");
elif (a%10==2 or a%10==3 or a%10==4) and (a%100<5 or a%100>20):
    print(a, "года");
else:
    print(a, "лет")
