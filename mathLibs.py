import numpy as np 
import math
import statistics
from time import sleep
import random

power_num = 2

"""
Demonstrates three math library functions: isqrt, fabs, and pow.
Takes user input and performs square root, absolute value, and power operations.
"""
def math_lib_functions():

    # Prompt user for input and remove whitespace
    usrnum_inp = input("Enter a non-negative whole number: ").strip()

    # Explcitly convert string input to an integer
    usrnum_sanit = int(usrnum_inp)

    # Print result of isqrt function
    int_sqrt = math.isqrt(usrnum_sanit)
    print(f"The square root of {usrnum_sanit} is {int_sqrt}")

    # Print result of fabs function
    int_absolute = math.fabs(usrnum_sanit)
    print(f"The absolute value of {usrnum_sanit} is {int_absolute}")

    # Print result of pow function
    int_pow = math.pow(usrnum_sanit, power_num)
    print(f"{usrnum_sanit} to the power of {power_num} = {int_pow}")


"""
Interactive number guessing game where user tries to guess a random number between 1-10.
Provides feedback if guess is too high or too low until correct number is guessed.
"""
def random_num_gen():
    # Generate random integer between 1 and 10
    random_int = random.randint(1, 11)
    # Initialize guess value to zero to set while loop condition
    usr_guess_int = 0 

    # Game introduction
    print("Time to test your luck!")
    print("-" * 60) ; sleep(.7)

    # Loop continues until user guesses the correct number
    while usr_guess_int != random_int:    
        try:
            usr_guess_int = int(input("Guess a number between 1-10: ")) # Implicitly convert input to an integer

            if usr_guess_int == random_int:
                print("Nice! You guessed right!")
                break
            elif usr_guess_int > random_int:
                print("Not quite, your guess is too high.")
            else:
                print("Incorrect, your guess is too low.")
        except ValueError:
            print("Invalid entry, try again...")


"""
Generates a random list of 10 numbers and allows user to calculate
statistical measures (mean, mode, median) from the list.
"""
def number_stat_info():
    print("-" * 60)
    print("This function checks the mean, mode, and median of the randomly generated list below")
    random_int_list = [random.randint(1, 100) for i in range(10)]
    print(random_int_list)
    print("-" * 60)

    while True:
        try:
            print("1: Mean")
            print("2: Mode")
            print("3: Median ")
            print("-" * 60)
            usr_numstat_choice = input("Enter a number to fetch the associated statistic: ").strip()
            print("-" * 60)
            if usr_numstat_choice.lower() == '1':
                # Calculate and display mean (average)
                print(f"Mean: {statistics.mean(random_int_list)}")
                print("-" * 60)
            elif usr_numstat_choice == '2':
                # Calculate and display mode (most frequent value)
                print(f"Mode: {statistics.mode(random_int_list)}")
                print("-" * 60)
            elif usr_numstat_choice == '3':
                # Calculate and display median (middle value)
                print(f"Median: {statistics.median(random_int_list)}")
                print("-" * 60)
            else:
                 # Exit program on any other input
                print("Exiting program...") ; sleep(0.7)
                return
            # Handle invalid inputs
        except ValueError:
            print("Invalid entry, try again...")


"""
Main menu that allows user to select which library demonstration to run.
"""
def main():
    print("-" * 55)
    print("               --- Python Libraries ---")
    print("-" * 55)
    print("1: (Math) Manipulate a number with math")
    print("2: (Random) Play a number guessing game")
    print("3: (Statistics) Statistics with python")
    print("-" * 55)

    try:
        usr_choice = input("Choose a library to demo: ").strip().lower()

        # Route user to specified function based on user_choice condition    
        if usr_choice == '1':
            math_lib_functions()
        elif usr_choice == '2':
            random_num_gen()
        elif usr_choice == '3':
            number_stat_info()
        # Exit program on any other input
        else:
            print("Exiting program...") ; sleep(0.7)
            return
    # Handle invalid menu inputs
    except ValueError:
        print("Invalid input, try again...")

# Runs main() when script is executed 
if __name__ == "__main__":
    main()