"""
Calculating the average of three numbers inputted by a user
**Key Concepts**
    - While loops (while True)
    - Loop interupt (break)
    - Datatype conversion (int(foo))
Faba Kouyate, Fall 2025
"""

def average_calculator():

    numsum = 0 # Initialized numsum to 0 to activate the loop

    while True:

        # Found this simple 'exit program' function on stackoverflow 
        quitFunction = input("\nType 'quit' to exit the calculator otherwise press enter: ")
        if quitFunction.lower() == 'quit':
            print("Exiting program")
            break # Recall what break is doing and how its different than return

        try: 
            # Retrieve three numbers from user
            num1 = input("Enter any number: ")
            num2 = input("Enter a second number: ")
            num3 = input("Enter a third number: ")
                
            # Convert inputs to integers
            num1_int = int(num1)
            num2_int = int(num2)
            num3_int = int(num3)

            # Calculate sum of all numbers and assign to a variable
            numsum = num1_int + num2_int + num3_int                                                                                   

            # Calculate average of both inputted numbers (sum of all numbers / total amount of numbers)
            average = float(numsum / 3)

            print("Calculation Complete")
            print(f"\nThe average of {num1_int}, {num2_int}, and {num3_int} is {average}")
    
        except ValueError:
            print("\n*Invalid entry* Enter a whole number.")
        

average_calculator()

