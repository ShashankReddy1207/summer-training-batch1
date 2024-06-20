#print the sum of highest prime number between the side by side elements of a list
def rec(a,b):
    while a<=b:
        c=0
        for i in range(2,b//2+1):
            if b%i==0:
                c=c+1
        if c==0:
            return b
        else:
            return rec(a,b-1)
    else:
        return 0
            
li=[14,16,20,22]
s=0
for i in range(len(li)-1):
    s=s+rec(li[i]+1,li[i+1]-1)
print(s)
    