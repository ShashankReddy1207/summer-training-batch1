#print the possible 3 combination values of a list using reccursion
def threepos(i,j,k,le):
    if i<j<k<le:
        print(l1[i],l1[j],l1[k])
        threepos(i,j,k+1,le)
    elif i<j<k and k==le:
        if j<le-2:
            j=j+1
            k=j+1
            threepos(i,j,k,le)
        else:
            i=i+1
            j=i+1
            k=j+1
            threepos(i,j,k,le)
l1=[3,2,5,4,1,6,8]
threepos(0,1,2,len(l1))
