#write a program to find if the given number is prime no or not
num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
          
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")
