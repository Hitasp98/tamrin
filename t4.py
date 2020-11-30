a=[]
for n in range (15):
    f=int(input("Enter your number : "))
    a.append(f)
for s in range (15):
    ma=0
    ss=s+1
    for ss in range (15):
        if a[s]>a[ss]:
            m=a[ss]
            a[ss]=a[s]
            a[s]=m
tmaxnumber=a[0]-a[14]
ttminnumber=a[0]-a[1]
for s in range (1,15):
    m=0
    m=a[s-1]-a[s]
    if ttminnumber<m:
           ttminnumber=m
            
print(a)
print("ekhtlafe tavali :",tmaxnumber)
print ("ekhtlafe motavali :",ttminnumber)
