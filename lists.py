"""
Faba Kouyate | Fall, 2025
"""
def list_comprehension():

    # Single data type list
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Mixed data type list
    x2 = [1, 'two', True, 4, 5j, 'six', 7, False, 9.0, 10] 

    # Intializing empty list (which will hold the nested list)
    nested_list = []
                                                                
    print("-" * 30)
    # Print the MAX value from the first list
    print(f"The MAX value from the first list: {max(x1)}")
    print("-" * 30)

    # Print the average value from the first list
    print(f"AVERAGE value of the first set: {sum(x1) / len(x1)}")
    print("-" * 30)

    # Print the list in the order of highest value to lowest
    x1.sort(reverse=True)
    print(f"x1 sorted from highest to lowest value: {x1}")
    print("-" * 30)

    for var in x2:
        if var == 5j:
            print(f"Specified value found: {var}")
            break
    print("-" * 30)

    for i in range(0, len(x2), 2):
        
        # Slices every two increments in the index and assigns each pair to section  
        section = x2[i : i + 2]

        # Append the pair to the empty list
        nested_list.append(section)

    # Print the new nested list
    print(f"Nested lists: {nested_list}")
    print("-" * 30)

list_comprehension()