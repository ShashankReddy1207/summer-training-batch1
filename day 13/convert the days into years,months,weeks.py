#convert the given days into years,months,weeks,days
y=300
m=30
w=6
dayss=65432
year=dayss//y
months=(dayss%y)//m
weeks=((dayss%y)%m)//w
days=((dayss%y)%m)%w
print(year,months,weeks,days)
