#return sum of even number from the given number using reccursion
def fa(x):
    if x==0:
        return 0
    return x+fa(x-2)
n=11
if n%2==0:
    print(fa(n))
else:
    print(fa(n-1))