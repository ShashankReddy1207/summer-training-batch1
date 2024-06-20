str="mmffmmfff"
c=0
le=len(str)
for i in str:
    if i=="m":
        c=c+1
    elif i=="f":
        c=c-1
if c==0:
    print(0)
elif c>0:
    print("m")
else:
    print("f")

        