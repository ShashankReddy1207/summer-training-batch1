class Node:
    def __init__(self, u):
        self.data = u
        self.nxt = None

class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end="->")
            t = t.nxt
        print("None")

    def addback(self, x):
        if self.head is None:
            self.head = Node(x)
        else:
            t = self.head
            while t.nxt is not None:
                t = t.nxt
            t.nxt = Node(x)

    def addeven(self):
        t = self.head
        s1 = 0
        while t is not None:
            if t.data % 2 == 0:
                s1 += t.data
            t = t.nxt
        print(s1)

    def sear(self, x):
        t = self.head
        while t is not None:
            if t.data == x:
                print("found")
                return
            t = t.nxt
        print("not found")

    def fastpoint(self):  # using fast and slow pointer print mid value
        t = self.head
        s = self.head
        while s is not None and s.nxt is not None:
            t = t.nxt
            s = s.nxt.nxt
        if s is None:
            print("even")
        else:
            print("odd")

    def lngsub(self):  # print the count of the sequential numbers in the list
        t = self.head
        c = 1
        m = 0
        while t.nxt is not None:
            if t.data + 1 == t.nxt.data:
                c += 1
            else:
                if c > m:
                    m = c
                c = 1
            t = t.nxt
        if c > m:
            m = c
        print(m)

    def pairing(self):
        t = self.head
        while t is not None and t.nxt is not None:
            k = t.nxt
            print(t.data, k.data)
            t = k.nxt

    def bubble_sort(self):
        if self.head is None:
            return
        t=self.head
        c=0
        end = None
        while t.nxt!=end:
            p = self.head
            f=0
            while p.nxt != end:
                q = p.nxt
                if p.data > q.data:
                    f=1
                    p.data, q.data = q.data, p.data
                p = p.nxt
                c=c+1
            end = p
            if f==0:
                break
        print(c)
    def rev(self):
        t=self.head
        c=0
        end = None
        while t.nxt!=end:
            p = self.head
            while p.nxt != end:
                q = p.nxt
                p.data, q.data = q.data, p.data
                p = p.nxt
                c=c+1
            end = p
        print(c)
    def rev1(self):
        a=self.head
        b=a.nxt
        while b.None:
            c=b.nxt
            b.nxt=a
            a=b
            b=c
        
            
            
        
l1 = SLL()
l1.addback(9)
l1.addback(8)
l1.addback(5)
l1.addback(4)
l1.addback(16)
l1.addback(15)


# l1.sear(10)
# l1.sear(202)
# l1.fastpoint()
# l1.lngsub()
# l1.pairing()
#l1.bubble_sort()
l1.rev1()
l1.display()
