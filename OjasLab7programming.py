#1
s = input("Enter a string: ")
reversed_str = ""
for char in s:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)
#2
sentence = input("Enter a sentence: ")
last_word_len = 0
current_len = 0
for char in sentence:
    if char == " ":
        if current_len > 0:
            last_word_len = current_len  
            current_len = 0  
    else:
        current_len += 1
if current_len > 0:
    last_word_len = current_len
print("Length of the last word:", last_word_len)
#3.1
s = input("Enter a sentence: ")
w = input("Enter a word to search: ")
if w in s:
    print(f"Yes, the word '{w}' exists in the sentence.")
else:
    print(f"No, the word '{w}' does not exist.")
print(f"The word '{w}' occurs {sentence.count(w)} time(s).")   
#3.2
 

#4
text = input("Enter a sentence: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for char in alphabet:
    if char not in text:
        is_pangram = False
        break

if is_pangram:
    print("It is a pangram!")
else:
    print("It is NOT a pangram.")
#5

#6
s = input("Enter a string: ")
n = len(s)
is_pal = True

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_pal = False
        break

if is_pal:
    print("It is a palindrome.")
else:
    print("It is NOT a palindrome.")
#8
n = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers = numbers + [num]
total_sum = 0
product = 1
smallest = numbers[0]
for x in numbers:
    total_sum += x
    product *= x
    if x < smallest:
      smallest = x
print("Sum of numbers:", total_sum)
print("Product of numbers:", product)
print("Smallest number:", smallest)
#11
p = input("Enter a paragraph: ")
digits = 0
alphabets = 0
special = 0
upper = 0
lower = 0

for char in p:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        alphabets += 1
        if char.isupper():
            upper += 1
        else:
            lower += 1
    else:
        special += 1

print(f"Alphabets: {alphabets} (Uppercase: {upper}, Lowercase: {lower})")
print(f"Digits: {digits}")
print(f"Special characters: {special}")
#12
s = input("Enter a string: ")
result = ""

for char in s:
    if char not in result:
        result += char

print("Without duplicates:", result)