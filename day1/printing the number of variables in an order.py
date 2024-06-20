#printing the number of variables in an order
list1="aaabbaaaaddd"
j=0
c=1
l2=""
m=len(list1)
while j<m-1:
    if list1[j]==list1[j+1]:
        c=c+1
        j=j+1
    else:
        c1=str(c)
        l2=l2+list1[j]+c1
        c=1
        j=j+1
l2=l2+list1[j+1]+str(c)
print(l2)    

        
        
    
    