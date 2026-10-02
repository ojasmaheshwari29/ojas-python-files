# #Project1
# salary = float(input("Enter your monthly salary: "))
# years = float(input("Enter years :"))

# if salary < 0 and years < 0:
#     print("Invalid")
    
# if years > 5:
#     bonus_percentage = 0.05
#     bonus_salary = bonus_percentage*salary 
#     print(f"Net bonus Amount: {bonus_salary:.2f}") 
# else:
#     print("Error, enter correct year")    

# #Project2
# password = input("Enter password")
# if password == "qwerty":
#     print("Welcome")
# else:
#     print("Wrong Password")   
    
# #Project3
# shape = input("Enter Shape:")
# if shape == "Square":
#     side = float(input("Enter side:"))
#     area = side*side
#     print(f"The area of square is {area:.2f}")
# elif shape == "Rectangle":
#     length = float(input("Enter the length:"))
#     width = float(input("Enter the Width:"))
#     area = length * width
#     print(f"The area of rectangle is {area:.2f}")    
# elif shape == "Circle":
#     radius = float(input("Enter radius:"))
#     area = 3.14 * radius * radius
#     print(f"The area of circle is {area:.2f}")    
# elif shape == "Triangle":
#     base = float(input("Enter the base:"))
#     height = float(input("Enter the height:"))
#     area = base * height / 2
#     print(f"The area of triangle is {area:.2f}")   
# else:
#     print("Invalid Shape")
    
# #project4
# hours = int(input("Enter Hours:"))    
# min = int(input("Enter minutes:"))
# total_min = hours*60 + min+15
# new_hours = (total_min//60)%24
# new_min = total_min %60
# print(f"{new_hours}:{new_min}")

# #project5
# n = float(input("Enter kilometers:"))     
# period = input("Enter day or night")    

# if period == "day":
#     taxi = 33.58 + n*37.89
# else:
#     taxi = 33.58 + n*43.17
# cheapest = taxi

# if n>= 20:
#     bus = n*4.32
    
#     if bus < cheapest:
#         cheapest = bus 
        
# if n >= 100:
#     train = n * 2.88 
#     train = n * 2.88
#     if train < cheapest:
#         cheapest = train
# print(f"Cheapest price: {cheapest:.2f} INR")   
    
    
# #project6
# holidays = int(input())
# total_days = 365
# workdays = total_days-holidays
# play_time_minutes = (workdays *63) + (holidays *127)

# norm = 30000
# difference =(norm -play_time_minutes )   
# hours = difference //60
# minutes = difference %60

# if play_time_minutes <= norm:
#     print("Tom sleeps well")
#     print(f"{hours}hours and {minutes}minutes")
# else:
#     print("tom will run away")   
#     print(f"{hours}hours and {minutes}minutes")
    
# #project7    
# budget = float(input("Enter budget: "))
# season = input("Enter season (summer or winter): ")

# destination = ""
# accommodation = ""
# spent_amount = 0.0

# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         accommodation = "Camp"
#         spent_amount = budget * 0.30
#     else:
#         accommodation = "Hotel"
#         spent_amount = budget * 0.70

# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         accommodation = "Camp"
#         spent_amount = budget * 0.40
#     else:
#         accommodation = "Hotel"
#         spent_amount = budget * 0.80

# else:
#     destination = "Europe"
#     accommodation = "Hotel"
#     spent_amount = budget * 0.90

# print(f"Somewhere in {destination}")
# print(f"{accommodation} - {spent_amount:.2f}")

#project8 
# for num in range(1, 1000):
#     if num % 10 == 6:
#         print(num)
 
#project9        
n = int(input("Enter total number of elements (n): "))
total_sum = 0

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    total_sum += num

print(f"Sum: {total_sum}")       
        