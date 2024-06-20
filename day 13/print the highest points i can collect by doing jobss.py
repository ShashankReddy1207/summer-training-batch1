l1=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
l2=[5,6,5,4,11,2]
le=len(l2)
l3=l2.copy()
for i in range(1,le):
    for j in range(0,i):
        if l1[j][1]<=l1[i][0]:
            if l3[j]<l3[j]+l2[i]:
                l3[i]=l3[j]+l2[i]
print(max(l3))