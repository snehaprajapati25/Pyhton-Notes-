# Loops in Python
# oops in Python allow us to execute a block of code multiple times without rewriting it

# Types of Loop
# 1. For Loop
a = range(1, 20, 1)

for i in range(1,20,1):
    print(i)

for i in range(20): #only end point is given
    print(i)

for i in range(20, 51): # from 20 to 50
    print(i)

for i in range(16, 0, -1): # from 16 to 1(reverse loop)
    print(i)


#lets print trable of 5
for i in range(5, 51, 5):
    print(i)


n = int(input("Enter the no: "))
# to print table of any n
# for i in (n, (n*10)+1, n):
#   print(i) 

for i in range(1,11):  
    print(f"{n*i}")


#For Loop on STRINGS
a = "SHERYIANS TEACHES INDUSTRY THINGS"
print(len(a))

for i in range(len(a)):
    print(a[i])


a = "SHERYIANS IS COOL"

for i in a:
    print(i)


##  Break
for i in range(1,21):
    if i==15:
        break  
    else:
        print(i)


## continue
for i in range(1,21):
    if i==15:
        continue
    else:
        print(i)


# Q1. Accept an integer and Print hello world n time
num = int(input("Enter the no: "))

for i in range(num):
    print("Hello World")


# Q2. Print table
num2 = int(input("Enter the no whose table u want to print: "))
for i in range(1,11):
    print(f"{num2} * {i} = {num2*i}")


# Q3. Sum up to n terms
n = int(input("Enter the no: "))
sum = 0

for i in range(1, n+1):
    sum += i
    print(f"your sum is{sum} ")


# Q4. Factorial of a numbe
n = int(input("Enter the no: "))

fact = 1;
for i in range(1, n+1):
    fact *= i
    print(f"your factorial is {fact} ")


# Q5. Print the sum of all even & odd numbers in a range separately

n = int(input("Enter the no: "))
evenSum = 0;
oddSum = 0;

for i in range(1, n+1):
    if i%2==0:
        evenSum+=i
    else:
        oddSum+=i
print( f"your even and odd sum are {evenSum}, {oddSum}")


# Q6. Accept a number and check if it a perfect number or not. 
#A number whose sum of factors is equal to the number itself 

n = int(input("Enter the no: "))
sum = 0

for i in range(1, n):
    if n%i == 0:
        sum += i

if sum == n:
    print("your no is perfect no.")
else:
    print("your no is not a perfect no.")


# Q7. Check wether the number is prime or no.
n = int(input("Enter the no: "))


if n <= 1:
    print(f"{n} is not a prime no.")
else: 
    for i in range(2, n):
        if n%i == 0:
           print(f"{n} is not a prime no.")
           break
    else:print(f"{n} is a prime no.")


# Q8. Reverse a string without using in build functions
a = "SHERYIANS"
b = ""
for i in range(len(a)-1, -1, -1):
    b+=a[i]
    print(b)



# Q9. Check string is Pallindrome or not
a = "SHERYIANS"
b = ""
for i in range(len(a)-1, -1, -1):
    b+=a[i]
    print(b)

if b==a:
    print(f"{a} is pallindrome")
else:
    print(f"{a} is not a pallindrome")



# Q10. Count all letters, digits, and special symbols from a given string 
a = "sakjhnwdf21346547#$%^^&"

char = 0
dig = 0
spchar = 0

for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1
        
print(f"your digits are {dig}\n your alphabets are {char}\n ypur special characters are {spchar}")
