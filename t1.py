a=[]

for n in range (10):
    f=int(input("Enter your number : "))
    a.append(f)
    if a[n] < 0:
        a[n]=a[n]*-1

for s in range (10):
    ma=0
    ss=s+1
    for ss in range (10):
        if a[s]>a[ss]:
            m=a[ss]
            a[ss]=a[s]
            a[s]=m

xx=a[1]*a[2]*a[3]
print(xx)
xx=xx**(1.0/3)
print (xx) 
