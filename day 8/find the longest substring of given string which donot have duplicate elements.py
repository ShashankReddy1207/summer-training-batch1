#find the longest substring of the string which donot have duplicate elements
s1="qwertyuiorplkjhgfdsazxcvbn"
s=""
le=len(s1)
j=0
m=0
for i in range(1,le):
    while j<le:
        if s1[j] not in s:
            s=s+s1[j]
            j=j+1
        else:
            if len(s)>m:
                m=len(s)
            s=""
            break
    j=i
print(m)
