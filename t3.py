a=int(input("Enter your name : "))
print(a//2)

ii=0
num=a
while ii<=2:
   if num > 1: 
     for i in range(2, num//2):
         num=num+1 
         if (num % i) == 0: 
             print(num, "is not a prime number")
             
         else:
             print(num, "is a prime number")
             ii=ii+1
             break
   else: 
      print(num, "is not a prime number")
   

 
 
