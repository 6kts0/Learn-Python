"""
FizzBuzz!
"""
# Define range
for i in range(1, 101):
    # optimal variables for fizzbuzz 
    fizz = i % 3 == 0  # these variables prevent ugly iff statements
    buzz = i % 5 == 0   
    if fizz and buzz:
        print("Fizzbuzz") # if i is divisible by 3 and 5 print "FizzBuzz"
    elif fizz:
        print("Fizz") # if i is divisible by 3 prints "Fizz"
    elif buzz:
        print("Buzz") # if i is divisible by 5 prints "Buzz"
    else:
        print(i) # when i is not divisible by either prints integer in range

