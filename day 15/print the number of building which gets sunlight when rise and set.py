#print the number of building which gets sunlight when rise and set
l1=[3,4,5,10,4,3]
c1=1
k=l1[0]
for i in range(1,len(l1)):
    if k<l1[i]:
        k=l1[i]
        c1=c1+1
print(c1)
c1=1
k=l1[-1]
for i in range(len(l1)-1,-1,-1):
    if k<l1[i]:
        k=l1[i]
        c1=c1+1
print(c1)
    
    