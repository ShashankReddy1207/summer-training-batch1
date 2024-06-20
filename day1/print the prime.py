#print the number if it is prime, else print the next prime number to the given number
def rec(n,c):
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=c+1
            break
    if c==0:
        print(n)
    else:
        rec(n+1,0)
n=int(input())
c=0
rec(n,c)