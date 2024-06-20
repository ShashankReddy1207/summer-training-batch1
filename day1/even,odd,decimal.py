#print the sum of even number,odd numebrs,decimal numbers seperatly in the given list 
list1=[5,3,7,5.6,4,2,3]
ec,oc,fc=0,0,0
for i in list1:
    if i%2==0:
        ec=ec+i
    elif int(i)==i and i%2!=0:
        oc=oc+i
    else:
        fc=fc+i   
print(ec)
print(oc)
print(fc)