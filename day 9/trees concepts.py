class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_tree:
    def create_node(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def display_inorder(self,root):
        if root is not None:
            self.display_inorder(root.left)
            print(root.data,end="->")
            self.display_inorder(root.right)
    def display_preorder(self,root):
        if root is not None:
            print(root.data,end="->")
            self.display_preorder(root.left)
            self.display_preorder(root.right)
    def display_postorder(self,root):
        if root is not None:
            self.display_postorder(root.left)
            self.display_postorder(root.right)
            print(root.data,end="->")
    def summ(self,t):
        if t==None:
            return 0
        return t.data+self.summ(t.left)+self.summ(t.right)
    def evensum(self,t):
        if t==None:
            return 0
        if t.data%2==0:
            return t.data+self.evensum(t.left)+self.evensum(t.right)
            
        else:
            return 0+self.evensum(t.left)+self.evensum(t.right)
    def oddsum(self,t):
        if t==None:
            return 0
        if t.data%2!=0:
            return t.data+self.oddsum(t.left)+self.oddsum(t.right)
            
        else:
            return self.oddsum(t.left)+self.oddsum(t.right)
    def difeo(self,t):
        if t==None:
            return 0
        if t.data%2==0:
            return self.difeo(t.left)+self.difeo(t.right)+t.data
        else:
            return self.difeo(t.left)+self.difeo(t.right)-t.data
    def heigh(self,t):
        if t==None:
            return -1
        return max(self.heigh(t.left),self.heigh(t.right))+1
    def leafcount(self,t):
        if t==None:
            return 0
        if t.left==None and t.right==None:
            return 1
        return self.leafcount(t.left)+self.leafcount(t.right)
    def leafsum(self,t):
        if t==None:
            return 0
        if t.left==None and t.right==None:
            return t.data
        return self.leafsum(t.left)+self.leafsum(t.right)
    def searcht(self,t,e):
        if t==0:
            return 0
        if t.data==e:
            return t.data
            
        elif e>t.data:
            return self.searcht(t.right,e)
        else:
            return self.searcht(t.left,e)
    def depth(self,t,e,c):
        if t.data==e:
            return c
        elif t.data<e:
            return self.depth(t.right,e,c+1)
        else:
            return self.depth(t.left,e,c+1)

    def bottomview(self,t):
        if t!=None:
            if t.left==None and t.right==None:
                print(t.data,end="->")
            self.bottomview(t.left)
            self.bottomview(t.right)
    def rightview(self,t,c,l1):
        if t!=None:
            if c not in l1:
                l1.append(c)
                print(t.data,end="->")
            self.rightview(t.right,c+1,l1)
            self.rightview(t.left,c+1,l1)
    def leftview(self,t,c,l1):
        if t!=None:
            if c not in l1:
                l1.append(c)
                print(t.data,end="->")
            self.leftview(t.left,c+1,l1)
            self.leftview(t.right,c+1,l1)
            
    def topview(self,t):
        if t!=None:
            d={}
            qq=[(t,0)]
            while qq:
                t=qq[0][0]
                if(t.left!=None):
                    qq.append((t.left,qq[0][1]-1))
                if(t.right!=None):
                    qq.append((t.right,qq[0][1]+1))
                if qq[0][1] not in d:
                    d[qq[0][1]]=t.data
                qq.pop(0)
            for i in sorted(d):
                print(d[i],end="->")
    def bottomview(self,t):
        if t!=None:
            d={}
            qq=[(t,0)]
            while qq:
                t=qq[0][0]
                if(t.left!=None):
                    qq.append((t.left,qq[0][1]-1))
                if(t.right!=None):
                    qq.append((t.right,qq[0][1]+1))
                d[qq[0][1]]=t.data
                qq.pop(0)
            for i in sorted(d):
                print(d[i],end="->")
tree=Binary_tree()
root=tree.create_node(20)
t=root
tree.insert(root,10)
tree.insert(root,29)
tree.insert(root,5) 
tree.insert(root,18)
tree.insert(root,22)
tree.insert(root,30)
tree.insert(root,17)
tree.insert(root,16)

 

#tree.display_inorder(root)
#print()
#tree.display_preorder(root)
#print()
#tree.display_postorder(root)
#print(tree.summ(t))#total sum
#print(tree.evensum(t))#odd number sum
#print(tree.oddsum(t))#even number sum
#print(abs(tree.difeo(t)))#difference of even and odd sum
"""t1=tree.heigh(t.left)
t2=tree.heigh(t.right)
if abs(t1-t2)==1 or abs(t1-t2)==0:
    print("yes")
else:
    print("no")"""
#print(tree.leafcount(t))#print count of leaf nodes
#print(tree.leafsum(t))#print sum of leaf node
"""val=int(input())
x=tree.searcht(t,val)
if x==val:
    print(tree.depth(t,val,0))
else:
    print("not found")
    """
"""l1=[]
tree.rightview(t,0,l1)
print()
l2=[]
tree.leftview(t,0,l2)"""
d={}
tree.topview(t)
print()
tree.bottomview(t)



