#check wheather the string contains all lowercase alphabates are not
st="the quiDFck brown fox jumps ove^&**r the lazy dog"
s1=""
for i in stt:
    if i.islower():
        s1=s1+i
s=set(s1)
if len(s)==26:
    print("yes")
else:
    print("no")


    

