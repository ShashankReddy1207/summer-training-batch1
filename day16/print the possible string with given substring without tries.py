q=int(input())
l1=[]
l2=[]
l3=[]
c=0
c1=0
for i in range(q):
    x=input()
    if x[0]=="1":
        l1.append(x[1:])
    elif x[0]=="4":
        if x[1:] in l1:
            l1.remove(x[1:])
    else:
        l2.append(x)
for i in l2:
    if i[0]=="2":
        for j in l1:
            if i[1:]==j:
                c=c+1
        if c!=0:
            print("True")
        else:
            print("False")
        c=0
    else:
        for j in l1:
            if i[1:]==j[:len(i[1:])] and i not in l3:
                c=c+1
                l3.append(i)
        if c!=0:
            print("True")
        else:
            print("False")
        print(c)
        c=0
print(l1)
print(l2)
        

        