a=int(input("enter number :"))
aa=a%10
print(aa)
s=0
if aa==1 or aa==3 or aa==5 or aa==7 or aa==9:
    for ss in range(a,100,2):
        print(ss)
        s=s+ss
print(s)
