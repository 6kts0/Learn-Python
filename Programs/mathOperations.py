import math
import time

emp_str = ""
user_num = 0

def valid_input_check():
    global user_num
    while True:
        try: 
            user_num_str = input("Enter a whole number or enter 'q' to exit: ")
            if user_num_str.lower().strip() == 'q':
                print("Exiting program...")
                break
            user_num = int(user_num_str)
            if user_num < 0:
                print("*INVALID* Enter a non-negative number")
            break
        except ValueError:
            print("*INVALID* Enter a non-negative whole number")


"""
Power of a Number
""" 
def multiply_user_num():
    print('-' * 55)
    print(f"{user_num} Squared: {user_num ** 2}") # Inputted number to the power of 2
    print('-' * 55)
    return

"""
Factorial of a Number
"""
def fact_user_num():
    print('-' * 55)
    print(f"The factorial of {user_num}: {math.factorial(user_num)}")
    print('-' * 55)
    return

"""
String Looping
"""
def rand_loop():
    global emp_str
    for i in range(user_num):
        emp_str += "*"
        print(emp_str)
        

def main():

    valid_input_check()

    print("\n--- MAIN MENU ---")
    print("1: Multiply your number by itself")
    print("2: Get the factorial of your number")
    print("3: Iterate a loop configured with your number")
    print("\nType 'x' followed by enter to exit the program")

    try:
        user_choice = input("\nEnter the operation you want to perform on your number: ")
        if user_choice.lower().strip() == 'x':
            print("Exiting program...")
            time.sleep(0.5)
            return
        elif user_choice == '1':
            multiply_user_num()
        elif user_choice == '2':
            fact_user_num()
        elif user_choice == '3':
            rand_loop()
    except ValueError:
        print("*INVALID INPUT* Enter one of the options listed")    
main()        