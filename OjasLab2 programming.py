

'''#1Divisibility by 5 
num = int(input("Enter a number: "))
if num % 5 == 0 :
    print("Hi")
else :
    print("Bye")
    
#2Area of Trapezoid
x = float(input("Enter the length of x side in meters :"))
y = float(input("Enter the length of y side in meters :"))
H = float(input("Enter the length of H side in meters :"))

Area = 0.5 * (x+y) * H
print("The area of trapezoid is :", Area)

#3BMI Interpreter
weight = float(input("Enter weight in kg :"))
height = float(input("Enter weight in meters :"))
bmi = weight / (height ** 2) 
print(f"Your BMI is: {bmi:.2f}")

if 0 < bmi < 18.5 :
    print("Underweight")
elif 18.5 < bmi < 25:
    print("Normal Weight")
elif 25 < bmi < 30:
    print("Slightly Overweight")
elif 30 < bmi < 35:
    print("Obese")    
else:
     print("Clinically Obese")
     
#4Bacterial Growth %
initial = 2.19e14
final = 4.68e14

growth_percentage = ((final - initial)/ initial) * 100 
print(f'Bacterial Growth: {round(growth_percentage)}%')

#5Time Converter 
total_months = int(input("Enter the number of months: "))

years = total_months // 12
remaining_months = total_months % 12
print(total_months, "is equal to" ,years, "Years and" ,remaining_months, "months")

#6Break even, profit loss
cost = float(input("Enter total cost:"))
total_revenue = float(input("enter Total revenue"))

if cost == total_revenue:
    print("break even")
elif total_revenue > cost:
    profit = total_revenue - cost 
    print(f"profit: {profit}")
else:
    loss = cost - total_revenue
    profit(f"Loss : {loss}")    
    
    
#7widget order cost calculation 
widgets_count = int(input("Enter number of widgets:"))

if 0 < widgets_count < 100:
    total_cost = widgets_count * 0.25  
else:
    total_cost = widgets_count * 0.20 
    
print("Total cost is ", total_cost)    

#8Vowel & Consonant Checker
char = input("Enter an alphabet:")
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
    print("Vowel")
else:
    print("Consonant")
    
#9Largest of 3 Numbers (Nested if-Else)
a = float(input("Enter num1:"))
b = float(input("Enter num2:"))  
c = float(input("Enter num3:")) 
if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print(f"The largest number is: {largest}")            

#10Gross Salary
salary = float(input("Enter your salary:"))

HRA = 0.20 * salary
TA = 0.05 * salary
DA = 0.10 * salary 

gross_salary = salary + HRA + TA + DA
print(f"gross_salary: Rs. {gross_salary:.2f}") 

#11Income Tax Slab identification
gross_salary = float(input("Enter your gross salary:"))

if gross_salary < 300000:
    tax_rate = "0%"
    tax_amount = 0.0
    
elif gross_salary <= 1000000:
    tax_rate = "10%"
    tax_amount = 0.10 * gross_salary
    
elif gross_salary <= 2500000:
    tax_rate = "20%"
    tax_amount = 0.20 * gross_salary
    
else:
    tax_rate = "30%"
    tax_amount = 0.30 * gross_salary
    
print(f"Income Tax Slab: {tax_rate} of the gross salary")
print(f"Tax_Amount: Rs. {tax_amount:.2f}")  

#12State Income Tax Flowchart Implementation 
income = float(input("Get taxable income: "))

if income <= 20000:
    tax = 0.20 * income
    
else:
    if income <= 50000:
        tax = 400 + 0.025 * (income - 2000)
    else:
        tax = 1150 + 0.035 * (income - 50000)
                
print(f"Display tax: {tax:.2f}")  

#13Weather forecasting    
color = input("Enter color")
mode = input("Enter mode")

if color == "blue" and mode == "steady":
    print("Steady blue, clear view.")
elif color == "blue" and mode == "flashing": 
    print("Steady blue, clouds ahead") 
elif color == "red" and mode == "steady":
     print("Steady red, rain ahead.") 
elif color == "red" and mode == "flashing":
    print("Flashing red, snow instead")
else:
    print("Invalid color or mode input.")    '''
          
          
#Cashier's Program 
pounds = float(input("Enter number of pounds of apples: "))
cash = float(input("Enter amount of cash tendered: ")) 

total_cost = pounds * 2.50 

if cash >= total_cost:
    change = cash - total_cost 
    print(f"Transaction successful. Your change is: ${change:.2f}")    
else:
    owed = total_cost - cash 
    print(f"You owe ${owed:.2f}more.")         
    

    
    
    
      
        






     

