#printing all the nodes of the graph using breadth first search
di={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8,9],8:[3,4,2,6],2:[8,4,1],1:[2],6:[8,10],10:[6],9:[3]}
q=[5]
v=[]
while q:
    for i in di[q[0]]:
        if i not in q and i not  in v:
            q.append(i)
    if q[0] not in v:
        v.append(q[0])
    q.pop(0)
print(v)
    
        
