import math 
# Log/Natural Log and Exponential Properties
# Precalculus lesson implementation 
# Problem: 4^(7x) = 5^(7x+10)

x = (10*math.log(5))/(7*(math.log(4)-math.log(5)))
print("Ex problem: 4^(7x) = 5^(7x+10)")
print(f"Solution: (Approximated): {x:.4f}") # Print approximation rounded to 4 decimal places 