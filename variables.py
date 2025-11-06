"""
Python is a dynamically typed, object oriented programming language.
"""


"""
1
"""
# Item input
product_str = input("Request Item: ")
# Generic input output
print("Chosen item: ", product_str + ".", "This item costs $14.99")

"""
2
"""
# Input integer cost
price_str = input("Verify the cost: ") 
# Convert input str to float
price_float = float(price_str)
# Give new float value an output variable
output_2 = f"Your item will cost ${price_float}"
# Print set output variable
print(output_2)

"""
3
"""
# Bag quantity input
transaction_end_str = input("How many bags would you like today: ")
# Convert str input to integer value
transaction_end_int = int(transaction_end_str)
# Output message with converted integer
print("Here are your", transaction_end_int, "bags")


