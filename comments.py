"""
Python is a dynamically typed, object oriented programming language.
"""


"""
string print statement
"""
print("15 points possible")

"""
f-string print statement
"""
average_weight = "5740 lbs" 

# Calling average_weight value
print(f"The average weight of a John Deer Tractor is {average_weight}")

"""
Boolean variables 
"""
x = 10
y = 5
# Print 
print(x > y)

"""
Fizz Buzz
"""
# Variable to check divisibility
b = 20 

# If 20 is a multiple of 5 print Fizz
if b % 5==0:
    print("Fizz")
# If 20 is a mutiple of 3 print Buzz    
elif b % 3==0:
    print("Buzz")
else: 
    print("N/A")

"""
Checking the struct type of an object 
"""
b = [1, 3, 5, 7]

print(type(b))


