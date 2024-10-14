print("Write the starting square column")
c1=input()
print("Write the starting square row")
r1=int(input())
print("Write the destination column")
c2=input()
print("Write the destination row")
r2=int(input())
if c1=="a":
    a1=1;
elif c1=="b":
    a1=2;
elif c1=="c":
    a1=3;
elif c1=="d":
    a1=4;
elif c1=="e":
    a1=5;
elif c1=="f":
    a1=6;
elif r1=="g":
    a1=7;
elif r1=="h":
    a1=8;
else:
    print("Well done! You've discovered a new row")
if c2=="a":
    a2=1;
elif c2=="b":
    a2=2;
elif c2=="c":
    a2=3;
elif c2=="d":
    a2=4;
elif c2=="e":
    a2=5;
elif c2=="f":
    a2=6;
elif c2=="g":
    a2=7;
elif c2=="h":
    a2=8
else:
    print("The piece had flown out of the board. Try again")
if (r1>8 or r1<1 or r2>8 or r2<1):
    print("Error 404. Row isn't found");
elif (r1-a1-r2+a2==0 or r1+a1-r2-a2==0 or r1==r2 or a1==a2) and (r1!=r2 or a1!=a2):
    print("YES");
else:
    print("NO")
