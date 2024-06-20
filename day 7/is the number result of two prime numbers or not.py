def primeadd(n,l1):
    c=0
    for i in range(4,n):
        for j in range(2,i//2+1):
            if i%j==0:
                c=c+1
        if c==0:
            l1.append(i)
        c=0
    c1=0
    print(l1)
    for i in range(len(l1)):
        for j in range(i,len(l1)):
            if l1[i]+l1[j]==n:
                print(l1[i],l1[j])
                return True
            
    else:
        return False
n=16
l1=[1,2,3]
print(primeadd(n,l1))

    
        

    