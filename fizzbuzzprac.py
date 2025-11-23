""" 
**Functionally coded fizzbuzz problem solution**
ORDER OF OPERATIONS MUST BE OBEYED
"""
import time
# Function starts
def fizzbuzz():
    # Added input method to define range
    strt_v = input("Enter a start value for a range: ")
    stp_v = input("Enter a stop value for your range: ")
    
    # Convert inputs to integers 
    start_value = int(strt_v)
    stop_value = int(stp_v)

    for i in range(start_value, stop_value):
        time.sleep(0.5) # Delete this to print range instantly

        # Pre-defined fizz and buzz (I ADDED THAT HYPHEN!!)
        fizz = i % 3 == 0
        buzz = i % 5 == 0

        if fizz and buzz:
            print("FizzBuzz")
        elif fizz:
            print("Fizz")
        elif buzz:
            print("Buzz")
        else:
            print(i)
fizzbuzz()