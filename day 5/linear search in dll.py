class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addend(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
    def addbeg(self,x):
        if self.head is None:
            self.head=node(x)
            self.tail=self.head
        else:
            newnode=node(x)
            newnode.next=self.head
            self.head.prev=newnode
            newnode.prev=None
            self.head=newnode
    def linearsearch(self,se):
        temp=self.head
        temp1=self.tail
        while temp!=temp1 and temp!=temp1.next :
            if temp.data==se or temp1.data==se:
                print("element found")
                break
            else:
                temp=temp.next
                temp1=temp1.prev
        if temp.data==se:
            print("element  found")
        else:
            print("element not found")
    def display(self):
        temp=self.head
        print("forward direction")
        while temp:
                print(temp.data,end=" ")
                if temp.next is not None:
                    print("<->",end=" ")
                temp=temp.next
        print()
        print("backward direction")
        temp=self.tail
        while temp!=None:
            print(temp.data,end=" ")
            if temp.prev is not None:
                print("<->",end=" ")
            temp=temp.prev
        print()
ll=dll()
ll.addbeg(4)
ll.addbeg(3)
ll.addend(5)
ll.addend(6)
ll.addend(10)
ll.display()
ll.linearsearch(5)
ll.linearsearch(2)
        
    
