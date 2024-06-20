st="lee*s*s*"
lis=list(map(str,st))
l1=[]
stt=""
for i in lis:
    if i=="*":
        l1.pop()
    else:
        l1.append(i)
stt=''.join(map(str,l1))
print(stt)

