#in the given list arrange 3 elements in ascending order from first to last
l1=[4,9,8,2,14,3,5,6]
for i in range(len(l1)-2):
    t=0
    if l1[i]>l1[i+1]:
        t=l1[i]
        l1[i]=l1[i+1]
        l1[i+1]=t
    if l1[i]>l1[i+2]:
        t=l1[i]
        l1[i]=l1[i+2]
        l1[i+2]=t
    if l1[i+1]>l1[i+2]:
        t=l1[i+1]
        l1[i+1]=l1[i+2]
        l1[i+2]=t
print(l1)
        
