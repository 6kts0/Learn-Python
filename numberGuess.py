"""
Python is a dynamically typed, object oriented programming language.

"""
import random

# Set a random value to guess
rnge_values = random.randint(1, 6)
rnge = rnge_values

# Get input value 
guess_in = input("Pick a number (1 - 10): ")

# Check for input value in rnge 
if guess_in == rnge:
    print("Nice!")
else:
    print(f"Try again... The number was {rnge_values}")