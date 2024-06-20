def rec1(e,l2,l3,id,le,y):
    if id==le:
        return l3
    else:
        if l2[id]%2!=0:
            y=y+e+l2[id]
            l3.append(y)
        return rec1(e,l2,l3,id+1,le,y)
    
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,9,6]
l3=[]
le=len(l2)
for i in l1:
    if i%2==0:
        rec1(i,l2,l3,0,le,0)
print(l3)
