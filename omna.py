# a = int(input("Enter a:"))2
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))

# if a>b and a>c:
#     print("a is the largest number")
# elif b>c:
#     print("b is the largest number")
# else:
#     print("c is the largest number")  

# year = int(input("Enter year:")) 
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
     
# units = float(input("Enter the number of units: "))
# if units < 0:
#         print("Units consumed cannot be negative.")
# else:
#     bill_amount = 0
#     if units <= 100:
#         bill_amount = units * 2
#     elif units <= 200:
#         bill_amount = (100 * 2) + ((units - 100) * 3)
#     elif units <= 300:
#         bill_amount = (100 * 2) + (100 * 3) + ((units - 200) * 5)
#     else:
#         bill_amount = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

# print(f"Total Electricity Bill: ₹{bill_amount:.2f}")

# a = int(input("Enter side a:"))
# b = int(input("Enter side b:"))
# c = int(input("Enter side c:"))

# if a<0 or b<0 or c<0 and a+b+c>180:
#     print("Invalid side")
# elif a == b==c:
#     print("Equilateral Triangle") 
# elif (a==b) or (b==c) or (c==a):
#     print("Isosceles Triangle")   
# else:
#     print("Scalene")     
# n = int(input("Enter any number"))
# if n%3==0:
#     print("Number is divisible by 3")
# else:
#     print("Number is not divisible by 3")    
# num = int(input("Enter any number"))
# if num%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")    
# age = int(input("Please enter your age:"))
# if age >18:
#     print("Old enough")
# else:
#     print("Too young")    
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# if a>b:
#     print("a is larger")
# elif b>a:
#     print("b is largest")
# else:
#     print("Integers are equal")        
# num = int(input("Enter any number:"))
# if num<0:
#     print("The number is negative")
# elif num>0:
#     print("The number is positive")    
# else:
#     print("The number is 0")    
# letter = str(input("Enter any letter"))
# vowel = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"  
# if letter == vowel:
#     print("True")
# else:
#     print("False")   
# for r in range(5,0,-1):
#     for c in range(r,0,-1):
#         print(c,end='')
#     print()
# for r in range(1,6):
#     for c in range(r,0,-1):
#         print(c,end='')
#     print()    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end='')    
#     print()   
# for i in range(1,6):
#     for j in range(4,i-1,-1):
#         print(" ",end='')
#     for c in range(0,i):
#         print("*",end='')     
#     print()    
# for r in range(1,6):

#     # printing the space
#     for c in range(4,r-1,-1):
#         print(' ',end='')

#     # printing the star
#     for c in range(0,r):
#         print('* ',end='')       # print the star with a space, it will make a triangle

#     print()
# s=0; n=2
# for i in range(1,11):
#     print(n)
#     s=s+n
#     n=n+2
# for i in range(20,0,-1):
#     print(i)
# n = 10
# for i in range(1,6):
#     print(n, end=" ")
# n = n*10 
# n=10
# for i in range(1,6):
#     print(n,end=' ')
#     n=n*10 
# for i in range(1,11):
#     print(i*i, end=" ") 
# s = 0
# for i in range(1,11):
#     s = s+i
#     print(s, end=" ")
# for i in range(10,100):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1     # counting the factors of i (value of i)

#     if fc==2:
#         fc=0
#         n=i+2       # taking another number from the current value of i with a difference of 2

#         for j in range(1,n+1):
#             if n%j==0:
#                 fc=fc+1     # counting the factors of n (value of n)

#         if fc==2:
#             print('(%d, %d)' %(i,n))
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print(chr(65+i), end="")
#     print()    
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print(chr(65+j), end="")
#     print() 
# n = 4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")    
#     print()  
# n = 4
# for i in range (1,n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()    
# n = 4
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()    
# n = 4
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    
# n = 4
# for i in range (n):
#     for j in range (n):
#         print("*",end=" ")
#     print()    
# n = int(input())
# for i in range(n):
#     for j in range (1,i+1):
#         print(j, end=" ")
#     print()    
# for i in range(5,0,-1):
#     print("*" * i)
# n = int(input("Enter n:"))
# for i in range (n):
#     print(i*(n-i-1))

    