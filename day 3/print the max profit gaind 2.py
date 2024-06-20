l1=list(map(int,input().split(" ")))
m=0
i=0
j=i+1
while i<j and j<len(l1):
    if l1[j]-l1[i]>m:
        m=l1[j]-l1[i]
    j=j+1
    if j==len(l1):
        i=i+1
        j=i+1
print(m)
     