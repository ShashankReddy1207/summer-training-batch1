di={5:[(3,8),(7,1)],7:[(3,6),(4,2),(5,1)],4:[(2,3),(7,2),(8,5)],8:[(2,4),(3,7),(4,5)],3:[(5,8),(7,6),(8,7)],2:[(4,3),(8,4)]}
def fun(x,l,di,s,t,m):
    l.append(x)
    if x==2:
        if s<m:
            t=l.copy()
            l.pop()
            return (t,s)
        l.pop()
        return (t,m)
    for i,j in di[x]:
        if i not in l:
            (t,m)=fun(i,l,di,s+j,t,m)
    l.pop()
    return (t,m)
l=[]
t=[]
print(fun(5,l,di,0,t,10000))





