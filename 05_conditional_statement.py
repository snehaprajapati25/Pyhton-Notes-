# conditional statements 
"""Conditional statements in Python allow decision-making by 
executing different blocks of code based on condition"""


# Types of conditional statements
"""1. if -  Executes if the condition is True
   2. if-else  -  Executes if True, another if false
   3. if-elif-else -  Checks multiple condition in sequence"""


# Q1. Accept two numbers and print the greatest between them.
a = input("Enter first no: ")
b = input("Enter second no: ")

if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print("Both the numbers are same.")


#  Q2. Accept the gender from the user as char and print the respective greeting message 

gender = (input("Enter your gender as character (M or F):"))

if gender=="M" or gender=="m":
    print("Good Morning Sir")
elif gender=="F" or gender=="f": 
    print("Good Morning Mam")
else:
    print("Unidentified Gender")


# Q3. Accept an integer and check whether it is an even number or odd.

p = int(input("Enter a number:"))

if p%2 == 0: 
    print(f"{p} is even no.")
else: 
    print(f"{p} is odd no.")


# Q4. Accept name and age from the user. Check if the user is a valid voter or not.

name = str(input("Enter your name: "))
age = int(input("Enter your age:"))

if age >= 18: 
    print(f"Hello {name} you are a valid voter.")
else: 
    print(f"Hello {name} you are not a valid voter.")


# Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)

year = int(input("Enter your year:"))

if (year%100 == 0 and year%400 == 0):
    print(f"{year} is a Leap Year")
elif year%100 != 0 and year%4 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")



#if -elif ladder
temp = int(input("Please tell the temperature: "))

if temp<0:
    print("Freezing Cold")

elif temp>=0 and temp<10:
    print("Very Cold")

elif temp>=10 and temp<20:
    print("Cold")

elif temp>=20 and temp<30:
    print("Pleasant")

elif temp>=30 and temp<40:
    print("Hot")
    
else:
    print("Very Hot")