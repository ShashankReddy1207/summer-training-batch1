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
    def update(self):
        temp=self.head
        temp1=self.tail
        s=self.tail
        while temp!=temp1.prev:
            temp=temp.next
            temp1=temp1.prev
        temp=self.head
        '''while temp1!=None:
            temp.data,temp1.data=temp1.data,temp.data
            temp=temp.next
            temp1=temp1.next'''
        s.next=temp
        temp1.prev.next=None
        temp.prev=s
        temp1=self.head
        temp1.prev=None
            
    def display(self):
        temp=self.head
        print("forward direction")
        while temp:
                print(temp.data,end=" ")
                if temp.next is not None:
                    print("<->",end=" ")
                temp=temp.next
        print()
        '''print("backward direction")
        temp=self.tail
        while temp!=None:
            print(temp.data,end=" ")
            if temp.prev is not None:
                print("<->",end=" ")
            temp=temp.prev
        print()'''
ll=dll()
ll.addend(3)
ll.addend(5)
ll.addend(7)
ll.addend(8)
ll.addend(9)
ll.addend(10)
ll.addend(12)
ll.addend(15)
ll.display()
ll.update()
ll.display()

        
    



