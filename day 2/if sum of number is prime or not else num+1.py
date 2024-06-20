#print the number if the sum of number is prime check the next number, do it untill we get the sum=prime
#eg=164 1+6+4  11 1+1 2-it is prime so return 164
#eg=166 1+6+6  13 1+3 4-it is not prime so check 167 1+6+7 14 1+4 5- is prime return 167
def div(m,n):
    i=0
    s=0
    for i in m:
        s=s+int(i)
    j=str(s)
    if len(j)>1:
        div(j,n)
    else:
        c=0
        if s in [2,3,5,7]:
            print(n)
        else:
            ss=int(n)
            div(str(ss+1),n+1)
            
            
n=int(input())
m=str(n)
div(m,n)