#print the largest even number by taking uniqe numbers from strings
st="tu5g2k1h8"
st1="g5g8gd6h3"
nu=""
for i in st:
    if i.isdigit() and i not in nu:
        nu=nu+i
for i in st1:
    if i.isdigit() and i not in nu:
        nu=nu+i
num=list(nu)
num.sort()
nu=num[::-1]
print(nu)
if int(nu[-1])%2==0:
    print(int("".join(nu)))
else:
    for i in range(len(nu)-2,-1,-1):
        if int(nu[i])%2==0:
            t=nu[i]
            nu[i]=nu[-1]
            nu[-1]=t
            k=i
            while(k<len(nu)-2):
                if nu[k]<nu[k+1]:
                    t=nu[k]
                    nu[k]=nu[k+1]
                    nu[k+1]=t
                k=k+1
            break
    print(int("".join(nu)))
    
    
    

