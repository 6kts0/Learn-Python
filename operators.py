
"""
Python is a dynamically typed, object oriented programming language.

Faba Kouyate | CS-87A
"""

# Define variables
x1 = 10
x2 = 2



"""
Arithmetic Operators
"""
# Addition -> Sum
add_input = input("Enter any integer to add: ")
add_conv = int(add_input)
print(x1 + add_conv)

# Subtraction -> Difference
sub_input = input("Enter any integer subtract: ")
sub_conv = int(sub_input)
print(x1 - sub_conv)

# Multiplication -> Product
mul_input = input("Enter any integer to  multiply: ")
mul_conv = int(mul_input)
print(x1 * mul_conv)

# Division -> Quotient
print(x1 / x2)

# Modulus -> Remainder
print(x1 % x2)

# Power -> Exponent 
print(x1 ** x2)

# Floor Division -> Quotient (integer only)
print(x1 // x2)


"""
Relational Operators
"""
# Equal to
print(x1 == x2)

# Not equal to
print(x1 != x2)

# Greater than
print(x1 > x2)

# Greater than or equal to
print(x1 >= x2)

# Less than
print(x1 < x2)

# Less than or equal to
print(x1 <= x2)


"""
Assignment Operators
"""
# Define main variable
main = 3

# Add and assign
a = main
a += 10 # a = a + 10
print(f"Add: {a}")

# Subtract and assign 
b = main 
b -= 2 # b = b - 2
print(f"Subtract: {b}")

# Multiply and assign
c = main
c *= 5 # c = c * 5
print(f"Multiply: {c}")

# Divide and assign 
d = main 
d /= 1.5 # a = a + 10
print(f"Division: {d}")

# Modulo and assign
e = main
e %= 1.5 # a = a + 10
print(f"Modulus : {e}")

# Power and assign
f = main
f **= 2
print(f"Exponentiation: {f}")

# Divide and assign (forces integer)
g = main
g //= 1.476
print(f"Floor Division: {g}")


"""
Logical Operators
"""
# and
# Returns True only if both conditions on its left and right are True
and_op = 10 > 2 and 2 < 10
print(f"Ten is greater than two and two is less than ten: {and_op}") 

# or 
#Returns True if at least one condition is True. It's only False if both are False
# Get input value
or_input = input("What number is equal to one: ")
conv_input = int(or_input)
or_op = (12 == 12 or 1 == conv_input)
print(f"Twelve is equal to twelve and one is equal to one: {or_op}")

# not
# Simply inverts the boolean value. It only takes one value, not two
not_op = not(1 > 2)
print(f"One is not greater than two: {not_op}") 


"""
Identity Operators
"""
# Define variables
x3 = [1, 2, 3]
x4 = [1, 2, 9]

# is 
print(x3 is x4)

# is not
print(x3 is not x4) 


"""
Membership Operators
"""
# Define variables
x5 = [1, 2, 3, 4, 5]

# in
# Returns True if it finds the specified value in the sequence, otherwise, it returns False
print(6 in x5)

# not in
#  Returns True if it cannot find the specified value in the sequence
print(2 not in x5)


"""
Bitwise Operators
"""
# AND
# Compares each bit position. The resulting bit is 1 only if both corresponding bits are 1
x6_input = input("Enter any integer: ")
conv_x6 = int(x6_input)
print(10 & conv_x6)

# OR
# Compares each bit position. The resulting bit is 1 if either of the corresponding bits is 1
x7_input = input("Enter any intger: ")
conv_x7 = int(x7_input)
print(20 | conv_x7)

# XOR
# Compares each bit position. The resulting bit is 1 only if the corresponding bits are different
x8_input = input("Enter any integer: ")
conv_x8 = int(x8_input)
print(6 ^ conv_x8)
                                                                   
# Not/Complement
# Flips all the bits of a single number (1s become 0s, 0s become 1s)
print(~10)

# Bitwise Left Shift
# Shifts all bits to the left by a specified number of places, padding the right side with zeros
print(10 << 2)

#Bitwise Right Shift
# Shifts all bits to the right, chopping off the bits that fall off the end
print(10 >> 2)