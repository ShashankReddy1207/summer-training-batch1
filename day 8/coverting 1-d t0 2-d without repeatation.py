#print the one-d list as 2-d list where the numbers are not repeated in the each sub list
#eg: 1,2,3,3,4,2,3
#  output:[[1,2,3,4],[3,2],[3]]
l1=[1,2,3,4,1,2,3,1,2]
s1=[]
le=len(l1)
while(1):
    s=[]
    for i in range(le):
        if(l1[i]!=-1):
            if l1[i] not in s:
                s.append(l1[i])
                l1[i]=-1
    if s==[]:
        break
    s1.append(s)
print(s1)
    
        