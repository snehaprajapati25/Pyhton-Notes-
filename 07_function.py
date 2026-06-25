# Functions
# Functions are reusable blocks of code that execute a specific task when called. This helps avoid repetition and makes programs modular and readable.
# To make your own function you have to use def keyword and then name the function. 

def hello():
    print("this is a hello function so i am doing hello")

hello()

# Types of arguments
# 1. positional arguments
def sum(a,b):
    print(f"sum of your numbers is {a+b}")

sum(3,4)


# 2. keyword argument 
def hello(name, age):
    print(f"Hello i am {name} and my age is {age}")

hello(age=23, name="John")


# 3. default argument
def sum(a,b=45):
    print(f"sum of your numbers is {a+b}")

sum(3)


## check if a string is plaindrome or not?
def pallindrome(st):
    rev = ""

    for i in range(len(st)-1, -1, -1):
        rev += st[i]

    if rev==st:
        print("pallindrome")
    else:
        print("not a pallindrome")

pallindrome("NAMAN")
pallindrome("CURSOR")


# use of return
def hello():
    return "hello how re u"

print(hello())