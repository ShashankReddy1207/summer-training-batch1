l1=[4,8,2,4,8,8,8]
le=len(l1)
c=1
w=l1[0]
i=1
while(i<le):
    if w==l1[i]:
        c=c+1
    else:
        if(c==0):
            c=c+1
            w=l1[i]
        else:
            c=c-1
            
    i=i+1
print(w)
    
    
    
    