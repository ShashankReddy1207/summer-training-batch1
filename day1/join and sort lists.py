#sorting two sorted lists as an other list
list1=[1,3,5,7]
list2=[2,3,6]
list3=[]
i=0
j=0
m=len(list1)
n=len(list2)
while i<m and j<n:
    if list1[i]<=list2[j]:
        list3.append(list1[i])
        i=i+1
    else :
        list3.append(list2[j])
        j=j+1
while i<m:
    list3.append(list1[i])
    i=i+1
while j<n:
    list3.append(list2[j])
    j=j+1
print(list3)