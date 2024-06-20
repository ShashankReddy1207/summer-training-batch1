h=[9,4,5,6,2,4]
li1=[]
li2=[]
li1.append(h[0])
for i in range(len(h)-1):
    if li1[i]<h[i+1]:
        li1.append(h[i+1])
    else:
        li1.append(max(li1))
print(li1)
li2.append(h[-1])
for i in range(len(h)-2,-1,-1):
    if li2[-1]<h[i]:
        li2.append(h[i])
    else:
        li2.append(li2[-1])
li22=li2[::-1]
print(li22)
c=0
for i in range(len(h)):
    c=c+(min(li1[i],li22[i])-h[i])
print(c)