"""
Python is a dynamically typed, object oriented programming language.
The value in a variable is a location in memory and the variable points to that location.
Faba Kouyate, Fall 2025
"""
numerator = 100
denominator = float(input("Enter a positive number: "))
result = 0

try:
    # Using "try" to run the erroneous code
    print("Trying the division...")
    result = numerator / denominator
    print("This line will not be reached.")

except ZeroDivisionError:
    # This block only runs if a ZeroDivisionError happens
    print("Error! You tried to divide by zero.")
    print("Setting result to 'None' (or 0, or some safe value).")
    result = None

# The program continues instead of crashing
print("-+" * 30)
print(f"The program continues.")
print(f"The final result is: {result}")

