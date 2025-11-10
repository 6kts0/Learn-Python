""" 
Functionally coded fizzbuzz problem solution
    * Acknowledge the order of operations necessary for this function to return properly
    * 
"""

# Start with defining a function with a parameter to acknowledge
def fizz_buzz():
    # Define a variable to hold "string" input
    str_user_input = input('Enter an integer between 1 and 101: ')

    # Convert input to integer
    integized_input = int(str_user_input)

    # Repeat request for smaller integer if input is above 100
    if integized_input > 100:
        back_up = input('Cannot exceed 100, enter an integer between 1 and 101: ')
        backup_integer = int(back_up)
        return backup_integer
    
    
    # Setup variables to hold fizz and buzz requirement
    fizz = integized_input % 3 == 0
    buzz = integized_input % 5 == 0

    # if, elif, else, operation outputs 
    if fizz and buzz:
        print('FizzBuzz')
    elif fizz:    
        print('Fizz')
    elif buzz:
        print('Buzz')
    else:
        print(integized_input)

fizz_buzz()