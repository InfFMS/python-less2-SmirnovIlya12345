a=int(input("Write an integer"))
b=[]
if a>=2:
    b.append(2);
if a>=3:
    b.append(3);
if a>=5:
    b.append(5);
if a>=7:
    b.append(7);
if a>=11:
    b.append(11);
if a>=13:
    b.append(13);
if a>=17:
    b.append(17);
if a>=17:
    b.append(19);
if a>=23:
    b.append(23);
if a>=29:
    b.append(29);
if a>=31:
    b.append(31);
if a>=37:
    b.append(37);
if a>=41:
    b.append(41);
if a>=43:
    b.append(43);
if a>=47:
    b.append(47);
if a>=53:
    b.append(53);
if a>=59:
    b.append(59);
if a>=61:
    b.append(61);
if a>=67:
    b.append(67);
if a>=71:
    b.append(71);
if a>=73:
    b.append(73);
if a>=79:
    b.append(79);
if a>=83:
    b.append(83);
if a>=89:
    b.append(89);
if a>=97:
    b.append(97);
for i in range(2, a):
    if (((i%2)*(i%3)*(i%5)*(i%7)*(i%11)*(i%13)*(i%17)*(i%19)*(i%23)*(i%29)*(i%31)*(i%37)*(i%41)*(i%43)*(i%47)*(i%53)*(i%59)*(i%61)*(i%67)*(i%71)*(i%73)*(i%79)*(i%83)*(i%89)*(i%97))!=0):
        b.append(i)
print(b)
