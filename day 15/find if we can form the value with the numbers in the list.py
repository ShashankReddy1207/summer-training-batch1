#find if we can form the value with the numbers in the list
l1=[2,3,5,6]
val=11
l2=[0]*(val+1)
l2[0]=1
l3=l2.copy()
for i in l1:
    for j in range(i,val+1):
        l3[j]=max(l2[j-i],l2[j])
    l2=l3.copy()
print(l3[-1])
        
    