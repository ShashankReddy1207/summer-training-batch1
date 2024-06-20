def rec1(e,l2,l3,id,le,y):
    if id==le:
        l3.append(y)
        return l3
    else:
        if l2[id]%2!=0:
            y=y+e+l2[id]
        return rec1(e,l2,l3,id+1,le,y)
    
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,9,6]
l3=[]
le=len(l2)
def rec2(l1,l2,l3,j,le):
    if j<le:
        if l1[j]%2==0:
            rec1(l1[j],l2,l3,0,le,0)
        return rec2(l1,l2,l3,j+1,le)
    else:
        return l3
print(rec2(l1,l2,l3,0,le))

        
    



