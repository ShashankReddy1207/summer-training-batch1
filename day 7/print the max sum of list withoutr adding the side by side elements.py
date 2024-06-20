def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)
l=[13,9,4,10,5,7]
print(fun(l))