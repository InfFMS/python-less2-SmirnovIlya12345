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
    c1=6;
elif r1=="g":
    c1=7;
elif r1=="h":
    c1=8;
else:
    print("Oh no! That's not a legal square")
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
    print("You can't move pieces out of the board")
if (r1>8 or r1<1 or r2>8 or r2<1):
    print("Go and play chess");
elif (r2-r1==2 and a2-a1==1) or (r2-r1==1 and a2-a1==2) or (r2-r1==-2 and a2-a1==1) or (r2-r1==-1 and a2-a1==2) or (r2-r1==2 and a2-a1==-1) or (r2-r1==1 and a2-a1==-3) or (r2-r1==-2 and a2-a1==-1) or (r2-r1==-2 and a2-a1==-1):
    print("YES");
else:
    print("NO")
