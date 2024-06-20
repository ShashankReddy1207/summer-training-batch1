
l1=list(map(int,input().split(" ")))
b=l1[0]
p=0
for i in range(1,len(l1)):
    if l1[i]<b:
        b=l1[i]
    if l1[i]-b>p:
        p=l1[i]-b
print(p)
    