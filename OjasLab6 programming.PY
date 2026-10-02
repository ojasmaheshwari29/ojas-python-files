# 1
# print("Addition Table")
# print("   ", end="")
# i = 1
# while i <= 9:
#     print(i, end=" ")
#     i = i + 1
# print()
# print("---------------------------------------")
# i = 1
# while i <= 9:
#     print(i, "|", end=" ")
#     j = 1
#     while j <= 9:
#         print(i + j, end=" ")
#         j = j + 1

#     print()
#     i = i + 1

# 2
# N = int(input("Enter N: "))
# if N <= 0 or N > 1000:
#     print("Invalid input")
# else:
#     slot = 1

#     while slot <= 1000:

#         if slot % N != 0:
#             slot = slot + 1
#             continue

#         if slot % 4 == 0:
#             slot = slot + 1
#             continue

#         print(slot, end=" ")
#         slot = slot + 1
# 
# 
# 3.1
# N = int(input("Enter N: "))

# if N <= 0:
#     print("Invalid input")
# else:
#     i = 1

#     while i <= N:
#         j = 1

#         while j <= i:
#             print(j, end=" ")
#             j = j + 1

#         print()
#         i = i + 1
# 3.2
# N = int(input("Enter N: "))

# if N <= 0:
#     print("Invalid input")
# else:
#     i = N

#     while i >= 1:
#         j = 1

#         while j <= i:
#             print("*", end=" ")
#             j = j + 1

#         print()
#         i = i - 1
# 3.3
# N = int(input("Enter N: "))

# if N <= 0:
#     print("Invalid input")
# else:
#     i = 1

#     while i <= N:
#         j = 1

#         while j <= i:
#             print("*", end=" ")
#             j = j + 1

#         print()
#         i = i + 1
# 5
# N = int(input("Enter number of students: "))

# if N < 2:
#     print("Invalid input")
# else:
#     maximum = -1
#     second = -1

#     i = 1

#     while i <= N:
#         distance = int(input("Enter distance: "))

#         if distance <= 0:
#             print("Invalid distance")
#         else:
#             if distance > maximum:
#                 second = maximum
#                 maximum = distance

#             elif distance < maximum and distance > second:
#                 second = distance

#         i = i + 1

#     print(maximum)
#     print(second)
# 6
# N = int(input("Enter N: "))

# if N <= 0:
#     print("Invalid input")
# else:
#     number = 1

#     while number <= N:

#         temp = number
#         digits = 0

#         while temp > 0:
#             digits = digits + 1
#             temp = temp // 10

#         temp = number
#         sum = 0

#         while temp > 0:
#             digit = temp % 10
#             sum = sum + digit ** digits
#             temp = temp // 10

#         if sum == number:
#             print(number, end=" ")

#         number = number + 1
# 9
# N = int(input("Enter N: "))

# if N <= 0:
#     print("Invalid input")
# else:
#     number = 1
#     i = 1

#     while i <= N:
#         j = 1

#         while j <= i:
#             print(number, end=" ")
#             number = number + 1
#             j = j + 1

#         print()
#         i = i + 1
# 10
# N = int(input("Enter odd N: "))

# if N <= 0 or N % 2 == 0:
#     print("Invalid input")
# else:
#     middle = N // 2 + 1

#     i = 1

#     while i <= middle:
#         spaces = middle - i
#         stars = 2 * i - 1

#         j = 1
#         while j <= spaces:
#             print(" ", end="")
#             j = j + 1

#         j = 1
#         while j <= stars:
#             print("*", end="")
#             j = j + 1

#         print()
#         i = i + 1

#     i = middle - 1

#     while i >= 1:
#         spaces = middle - i
#         stars = 2 * i - 1

#         j = 1
#         while j <= spaces:
#             print(" ", end="")
#             j = j + 1

#         j = 1
#         while j <= stars:
#             print("*", end="")
#             j = j + 1

#         print()
#         i = i - 1
# 7
# N = 1
# while N <= 15:
#     square = N * N
#     cube = N * N * N
#     square_root = N ** 0.5
#     print(N, "\t", square, "\t", cube, "\t", format(square_root, ".4f"))   
#     N = N + 1
# 8.1 
# n = int(input("enter number n: "))
# for i in range(1, n + 1):
#      for j in range(n - i):
#             print("  ", end="")
#      for j in range(i):
#             print(i, end=" ")
# 8.2
# N = int(input("Enter number of lines: "))

# for i in range(1, N + 1):
#     print(" " * (N - i), end="")

#     for j in range(i):
#         print(i, end=" ")

#     print()      
