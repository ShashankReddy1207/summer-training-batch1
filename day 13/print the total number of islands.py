#print the total number of islands
def fun(l1,m,n):
    if m<0 or n<0 or m>=len(l1) or n>=len(l1) or l1[m][n]!=1:
        return 
    if l1[m][n]==1:
        l1[m][n]=2
        fun(l1,m-1,n)
        fun(l1,m,n-1)
        fun(l1,m+1,n)
        fun(l1,m,n+1)
l1=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
c=0
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i][j]==1:
            fun(l1,i,j)
            c=c+1
print(c)
    
        