#print the string with the vowel characters as uppercase and consonents as lowercase
list1='education'
list2=''
for i in list1:
    if i.isupper():
        if i not in 'AEIOU':
            list2=list2+i.lower()
        else:
            list2=list2+i
    elif i.islower():
        if i in 'aeiou':
            list2=list2+i.upper()
        else:
            list2=list2+i
print(list2)
