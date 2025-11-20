"""
A string is an array of characters
Faba Kouyate | Fall 2025
"""

def string_manipulation():

    # Intialize string_in  
    string_in = ""

    # Check if input is at least 10 chars long
    while len(string_in) < 10:
        # Get the input 
        string_in = input("Enter a string at least 10 chars long: ")
        try: 
            if len(string_in) < 10:
                raise ValueError    
        except ValueError:
            print("*INVALID INPUT* | Enter a string with at least 10 chars")

    # Lower case conversion
    # checking lower conversion
    lower_string = string_in.lower()
    print(f"Lowercased: {lower_string}")
    print(f"{lower_string.islower()}, the string is lowercase")

    # Upper case conversion
    # Checking upper conversion
    upper_string = string_in.upper()
    print(f"Uppercased: {upper_string}")
    print(f"{upper_string.isupper()}, the string is uppercase")

    # Split the original input into two parts starting at the fifth char
    split_half = string_in[5:]
    split_half2 = string_in[:5]
    # Concatenate splits into one string
    print(f"Split string starting at the 5th char: {split_half2} and {split_half}")
    print(f"Concatenated split strings: {split_half2 + split_half}")

    # Remove the first char
    first_char_remove = string_in[1:]
    # Remove the last char
    last_char_remove = string_in[:-1]
    print(f"Removed FIRST character: {first_char_remove}")
    print(f"Removed LAST character: {last_char_remove}")

    # Remove all instances of 'i' and replace with empty value
    specified_char_remove = string_in.replace("i", "")
    print(f"All instances of 'i' removed: {specified_char_remove}")
    # Replace all instances of 'i' with '0'
    specified_char_replace = string_in.replace("i", "0")
    print(f"All instances of 'i' replaced: {specified_char_replace}")

    print("+-" * 20)

    # Iterate through the string and print each character
    for char in string_in:
        print(char, end="-")

string_manipulation()