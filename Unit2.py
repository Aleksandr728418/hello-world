pi = 3.14
radius = 6
circumference = 2*pi*radius
print(f"The circle with radius = {radius} has circumference = {circumference}")
radius = 15
circumference = 2*pi*radius
print(f"The circle with radius = {radius} has circumference = {circumference}")
##task 2.1

# DO NOT TOUCH THE FOLLOWING LINES 4, 5 and 6
# THESE ARE USED FOR THE TESTS. 

a = int(input("Please enter a number: ")) # leave this line alone
b = int(input("Please enter a number: ")) # leave this line alone
c = int(input("Please enter a number: ")) # leave this line alone

# TASK 1. 
# print out the type of 10.3 + 5
print(type(10.3+5))
# TASK 2.
# print(a + b * c) # Correct this so that the ``+`` is evaluated first
print((a+b)*c)
# print(a**b+c)    # Correct this so that the exponent is b+c
print(a**(b+c))
# TASK 3. 
# print the output of a < b
print(a<b)
# TASK 4. 
# print the output of (a < b) == (a <= b)
print((a < b) == (a <= b))