list1="74552333"
c=0
cc=0
for i in list1:
    s=int(i)
    for i in range(2,(s//2)+1):
        if s%i==0:
            c=c+1
    if(c==1):
        cc=cc+1
            
print(cc)

    
        
    
    