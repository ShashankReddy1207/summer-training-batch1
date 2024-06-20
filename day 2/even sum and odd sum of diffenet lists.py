#return sum of the even elements in one list and sum of odd elements in other list using reccursion
def rec(i,sa):
    if i==len(a):
        return sa
    if a[i]%2==0:
        sa=sa+a[i]
    
    return rec(i+1,sa)
def rec1(i,sb):
    if i==len(b):
        return sb
    if b[i]%2!=0:
        sb=sb+b[i]
    return rec1(i+1,sb)
        
a=[2,3,4,5]
b=[3,5,6,9,3]
print(rec(0,0),rec1(0,0))


