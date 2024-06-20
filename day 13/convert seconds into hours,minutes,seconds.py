#convert the given seconds into hours,minutes,seconds
h=60
m=60
seconds=6543
hr=seconds//(h*h)
mi=(seconds%(h*h))//m
se=(seconds%h)%m
print(hr,mi,se)

