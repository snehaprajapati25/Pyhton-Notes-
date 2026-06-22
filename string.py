# string and type conversion

a = "a"
print(ord(a)) #ord() converts a character to its ASCII numbe(unicode i.e 97)

b = 89
print(chr(b))#chr() converts a number to its corresponding character (unicode i.e Y)


#string indexing
name = "harsh coder"
print(name[0]) #h
print(name[-1], name[4]) #h h

#string slicing
print(name[0:5:1]) #harsh name[start:stop:step]  stop will aoways be stop-1(if u wrirt3 it will slice(prinmt) upto 2)
print(name[0::1]) #harsh coder (nothing written means goes upo default end point)
# print(naame[::]) 



# type conversion
int(), float(), str(), bool()

a = 12
a= str(a)
print(type(a)) #<class 'str'>

b = "132"
b = int(b)
print(type(b)) #<class 'int'>


c = 0
print(bool(c)) #False (0 is always False)

# Falsy values in Python are: False, 0, 0.0, "", [], (), {}.


# Type conversion types in Python:
# 1. Implicit Type Conversion (Type Coercion): In this python automatically converts data from one data type to another.v

print(5 + 3.2) #8.2 (int is converted to float)

#2. Explicit Type Conversion (Type Casting): In this we manually convert data from one type to another using built-in functions like int(), float(), str(), etc.