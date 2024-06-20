"""
eq=3
    abc
    efg
    hij
    aehbf -true
    aafghi - false
    
"""
n=int(input())
ma=[]
for i in range(n):
    cr=input()
    ma.append(cr)
s=input()
le=len(s)
j=0
i=0
c=0
s1=[]
while i<n and j<len(s):
    if s[j] in ma[i%n]:
        c=c+1
        j=j+1
        i=i+1
    else:
        print("false")
        break
    
if c==le:
    print("true")


        
    


        