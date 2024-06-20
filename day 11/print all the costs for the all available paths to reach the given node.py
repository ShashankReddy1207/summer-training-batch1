di={5:[(7,5),(3,4)],7:[(5,5),(4,2),(3,7)],4:[(7,2),(8,1),(2,3)],3:[(5,4),(7,7),(8,6)],8:[(3,6),(4,1),(2,1)],2:[(8,1),(4,3)]}
def fun(x,l,di,s):
    l.append(x)
    if x==2:
        print(l,s)
    for i,j in di[x]:
        if i not in l:
            fun(i,l,di,s=s+j)
    l.pop()
            
l=[]
fun(5,l,di,0)



