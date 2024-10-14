print("Write the month number")
a=int(input())
if a<3:
    print("Winter");
elif a<6:
    print("Spring");
elif a<9:
    print("Summer");
elif a<12:
    print("Fall");
elif a==12:
    print("Winter");
else:
    print("Congrats! You've invented a new calendar!")
