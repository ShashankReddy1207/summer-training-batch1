#print the size of the largest island
def fun(l1,m,n,c1):
    if m<0 or n<0 or m>=len(l1) or n>=len(l1) or l1[m][n]!=1:
        return c1
    if l1[m][n]==1:
        l1[m][n]=2
        c1=c1+1
        c1=fun(l1,m-1,n,c1)
        c1=fun(l1,m,n-1,c1)
        c1=fun(l1,m+1,n,c1)
        c1=fun(l1,m,n+1,c1)
    return c1
l1=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
c=0
ma=0
c1=0
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i][j]==1:
           c1=fun(l1,i,j,0)
           if ma<c1:
               ma=c1
    
print(ma)
    
        
