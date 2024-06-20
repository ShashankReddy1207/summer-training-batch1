#print the count of maximum number of continuos letter in string
s="yabcde"
c=1
m=0
i=0
j=i+1
while(i<j and j<len(s)):
    if ord(s[i])+1==ord(s[j]):
        c=c+1
        i=i+1
        j=i+1
    else:
        if m<=c:
            m=c
        c=1
        i=i+1
        j=i+1
if(c>m):
    m=c
print(m)
    
    
    
