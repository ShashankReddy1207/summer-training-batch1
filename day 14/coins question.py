c=[1,3,4,5]
n=17
m=[-1]*(n+1)
m[0]=0
for i in c:
    for j in range(1,n+1):
        if i<=j:
            x=(j-i)
            if m[j-i]!=-1:
                if m[j]!=-1:
                    m[j]=min(m[j],m[j-i]+1)
                else:
                    m[j]=m[x]+1
print(m)
print(m[-1])