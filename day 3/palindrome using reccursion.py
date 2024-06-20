def re(n,s):
    if(n>0):
        s=s*10+(n%10)
        return re(n//10,s)
    else:
        return s
n=12321
s=0
x=re(n,s)
print(x)
if x==n:
    print("yes")
else:
    print("no")
