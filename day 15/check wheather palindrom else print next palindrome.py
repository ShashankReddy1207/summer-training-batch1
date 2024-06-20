n=input()
s=""
if len(n)%2==0:
    s=s+n[:len(n)//2]+n[:len(n)//2][::-1]
    if int(s)>int(n):
        print(int(s))
    else:
        s=""
        s=s+n[:(len(n)//2)-1]+str(int(n[len(n)//2])+1)
        s=s+s[::-1]
        print(s)
else:
    s=s+n[:len(n)//2]+n[(len(n)//2)+1]+n[:len(n)//2][::-1]
    if int(s)>int(n):
        print(int(s))
    else:
        s=""
        s=s+n[:len(n)//2]+str(int(n[(len(n)//2)+1])+1)+n[:len(n)//2][::-1]
        print(s)

    
        
    
        
        