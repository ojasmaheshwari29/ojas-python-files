#project -1:
#print("Hello JKLU! and i am learning python")

#project -2:
# name = str(input("please enter your name:"))
# branch_name = str(input("please enter your branch name:"))
# print("welcome",name,"to",branch_name,"branch")

# prject -3:
# length = int(input("enter a length:"))
# width = int(input("enter a width"))
# area = length* width 
# print("the area of rectangle is",area,"sqm")

# project -4:
# length = int(input("enter a length:"))
# width = int(input("enter a width:"))
# len2 = length*0.305 #feet to meter 
# width2 = width*0.305
# area = len2*width2
# print("the area of rectangle is",area,"sqm")

#project -5:
# x = int(input("please enter the positive number x:" ))
# y = int(input("please enter the positive number y;"))
# if x>0 and y>0 :
#     if y % x ==0:
#         print("y is divisible by x")
#     else:
#         print("y is not divisible by x")
# else:
#     print("invalid input")            

#project -6:
# integer = int(input("enter a number:"))
# if integer % 2 == 0:
#     print("even")
# else:
#     print("odd")   


# project -7 :
# radius  = int(input("enter the radius:"))
# if 1 <= radius <=100:
#    area = ("3.14"* radius* radius)
#    print("the area of circle:",area)
# else:
#    print("invalid radius")

#project -8:
# temp_celcius = int(input("enter temp:"))
# faherenheit =(temp_celcius*9 / 5)+32
# kelvin = temp_celcius + 273.15
# print("the temp.in faherenheit is:",faherenheit)
# print("the temp.in kelvin is :",kelvin)

#project - 9:
seconds = int(input("Enter time in seconds"))
hours = seconds//3600
minutes = (seconds%3600)//60
secs = seconds%60

print(f"{hours:02}:{minutes:02}:{secs:02}")