#Lab 5(5)#

#1#

# X=int(input())
# Y=int(input())
# N=int(input())
# count=0
# for i in range (X,Y):
#     if i%N!=0:
#         print(i,end=' ')
#         count+=1
# print("\n",count)


#2#

#1st Method#

# n = int(input("Enter positive integer "))
# mul = 1
# while n>0:
#     digit = n%10
#     mul = mul*digit
#     n=n//10
# print(mul)

#2nd Method#

# a=int(input())
# b=0
# c=None
# while a>0:
#     b=a%10
#     if c is None:
#         c=b
#     else:
#         c=c*b
#     a=a//10
# print(c)

#3#

# n=int(input())
# large=0
# small=0
# bill=int(input())
# while bill != -999:
#     if bill>n:
#         large+=1
#     else:
#         small+=1
#     bill=int(input())
# print(large)
# print(small)


#4#

# n=int(input("Enter n "))
# p=int(input("Enter p "))
# if n<=0 and p<=0:
#     print("Invalid input")
# else:
#     result = 1 p
# while p>0:
#     result*=n
#     p-=1
# print(result)


#5#

# a=int(input())
# b=int(input())
# d=0
# while a>0:
#     c=a%10
#     d=d*10+c
#     a=a//10
# if d==b:
#     print("Numbers are reverse of each other")
# else:
#     print("Numbers are not reverse")


#6#

# n=int(input("Enter number: "))
# power=1
# for i in range(n):
#     if i == n-1:
#         print(power)
#     else:
#         print(power, end=" ")
#     power*=2


#8#

# n=int(input())
# for i in range(1,n+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()


#9#

# a=int(input("enter your number:"))
# D=int(input("enter a digit:"))
# if 0<=D<=9:
#     pass
# else:
#     print("invalid digit")
#     D=int(input("enter a digit:"))
# count=0
# while a>0:
#     b=a%10
#     a=a//10
#     if b==D:
#         count+=1
#     else:
#         continue
# print("Number of times digit is repeated:",count)


#10#

# a=int(input())
# b=0
# count=0
# for i in range(1,a):
#     if a%i==0:
#         print(i)
#         count+=1
# if count==1:
#     print("It's a Prime Number")
# else:
#     print("It's not a Prime Number")