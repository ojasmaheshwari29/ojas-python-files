# S = input("Ojas Maheshwari ")
# # for i in S:
# for i in range(len(S)):
#     print(S[i])

# print("HELLO WORLD")

# s = input("Enter String:")
# space_count=0
# digit_count=0
# alpha_count=0
# special_count=0
# for ch in s:
#     if ch in " ":
#         space_count +=1
#     elif ch in "123456789":
#         digit_count +=1
#     elif ch.lower() in "abcdefghijklmnopqrstuvwxyz":
#         alpha_count+=1
#     else:
#         special_count+=1    
# print()        
# s = input("enter string") 
# rev = " "
# for i in s:
#     rev=i+rev
# print(rev)              
# s = input("enter string ")
# for i in range (len(s)-1,0,-1):
#     print(s[i-1],end="")  

#2. Lecture#

# marks = [76,67,90,69,58]
# total = 0
'''for m in marks:
    total+=m
print(total/len(marks))'''
# for i in range(len(marks)):
    # total+=marks[i]
# print(total/(i+1))

## max function on the list ##

'''numbers = [10, 24, 76, 23, 12]
largest_number = max(numbers)
print(largest_number)'''

'''numbers = [10, 24, 76, 23, 12]
if numbers:
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    print("The maximum value is:", max_value)
else:
    print("The list is empty.")'''
    
# big=0
# for i in marks:
#     if i>big:
#         big=i
# print(big)

'''marks = [76,67,90,69,58]
marks.append(95)
marks.insert(1,78)
marks.pop()
marks.sort()
marks.remove(67)
marks.sort()
marks.reverse()
print(marks)'''

# marks = [76, 67, 90, 69, 58]
# marks.append(95)
# marks.insert(1, 78)
# marks.pop()
# marks.remove(67)
# marks.sort(reverse=True) 
# print(marks) 