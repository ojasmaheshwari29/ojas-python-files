#Project1
'''import math
x1 = float(input("Enter x-coordinate (x1): "))
y1 = float(input("Enter y-coordinate (y1): "))
r = float(input("Enter the radius of the circle (r): "))

# Step 2: Prompt the user for the target point coordinates
print("\n--- Target Point ---")
x2 = float(input("Enter point x-coordinate (x2): "))
y2 = float(input("Enter point y-coordinate (y2): "))

# Step 3: Compute the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Step 4: Compare distance with radius and display results
print("\n--- Result ---")
print(f"Calculated Distance: {distance:.4f}")

if distance < r:
    print(f"The point ({x2}, {y2}) lies INSIDE the circle.")
elif distance == r:
    print(f"The point ({x2}, {y2}) lies ON THE BOUNDARY of the circle.")
else:
    print(f"The point ({x2}, {y2}) lies OUTSIDE the circle.")  
    
#Project2
import math
side = float(input("Enter the side of a regular pentagon: "))
numerator = 5 * (side ** 2)
denominator = 4 * math.tan(math.pi / 5)
area = numerator / denominator

# Display the result
print(f"The area of the pentagon is: {area:.2f}")  

#Project3
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

# Check whether the angles can form a triangle
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid angles. Angles must be greater than 0.")

elif a + b + c != 180:
    print("The angles cannot form a triangle.")

else:
    print("The angles can form a triangle.")

    # Classify the triangle
    if a == 90 or b == 90 or c == 90:
        print("It is a Right-Angled Triangle.")

    elif a > 90 or b > 90 or c > 90:
        print("It is an Obtuse-Angled Triangle.")

    else:
        print("It is an Acute-Angled Triangle.")
        
#Project4
num = input("Enter a 4-digit number: ")
sum_first_two = int(num[0]) + int(num[1])
sum_last_two = int(num[2]) + int(num[3])
print(f"Sum of first two digits: {sum_first_two}")
print(f"Sum of last two digits: {sum_last_two}")

if sum_first_two == sum_last_two:
    print("The sums are equal.")
else:
    print("The sums are not equal.")      
    
#Project5
num = int(input("Enter 5 digit number: "))
d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10
max_digit = d1
pos = 1
if d2 > max_digit:
    max_digit = d2
    pos = 2
if d3 > max_digit:
    max_digit = d3
    pos = 3
if d4 > max_digit:
    max_digit = d4
    pos = 4
if d5 > max_digit:
    max_digit = d5
    pos = 5
print("Largest digit:", max_digit)
print("Position from left:", pos)

#Project6
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

#
a = a + b + c  # 'a' now holds the total sum (60)
b = a - (b + c)  # 'b' gets the original value of 'a' 
c = a - (b + c)  # 'c' gets the original value of 'b' 
a = a - (b + c)  # 'a' gets the original value of 'c' 

print(f"a = {a}, b = {b}, c = {c}")

#Project7
number = int(input("Enter a 3-digit number: "))

# Extract each digit using integer division and modulus
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

# Calculate the sum of the digits
digit_sum = hundreds + tens + ones

# Check if the number is divisible by the sum of its digits
if number % digit_sum == 0:
    print(number, "is a Harshad number.")
else:
    print(number, "is NOT a Harshad number.") 

#Project7
V = float(input("Enter the initial quantity of water (V in litres): "))
N = int(input("Enter the number of days (N): "))

if V < 0 or N < 0:
        print("Error: Water quantity and days cannot be negative.")
else:
    quantity = 200 + (V - 200) * (0.95**N)
print(f"The quantity of water in the tank after {N} days is {quantity:.2f} litres.")  

#Project9 

a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

   
a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

    # Calculate determinants
D = (a1 * b2) - (a2 * b1)
Dx = (c1 * b2) - (c2 * b1)
Dy = (a1 * c2) - (a2 * c1)
# Check for parallel or coincident lines
if D == 0:
    if Dx == 0 and Dy == 0:
        print("\nThe lines are coincident (they are the same line and have infinitely many intersections).")
    else:
        print("\nThe lines are parallel (they never intersect).")
else:
        
    x = Dx / D
    y = Dy / D
    print(f"\nThe point of intersection is: ({x:.2f}, {y:.2f})")'''

