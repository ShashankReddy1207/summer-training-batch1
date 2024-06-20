#Print all the nodes present in the graph
di={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8],8:[3,4,2],2:[8,4]}
def fun(x,l,di):
    l.append(x)
    for i in di[x]:
        if i not in l:
            fun(i,l,di)
l=[]
fun(5,l,di)
print(l)
