import csv
import time

# Define main constants
BAL_DATA = "balanceCorrelation.csv"
ROWS_10 = 10
HEAD_DISPLAY = ['Name' ' | ' 'Occupation' ' | ' 'Net Worth']
HEAD = ['first_name', 'job_title', 'balance']
# -------------------------------------------------- # 
NME = 'first_name'
JOB = 'job_title'
BAL = 'balance'

# Used only in row_display()
ROW_RANGE = range(199, 220)


"""
Display First Ten Rows
"""
def row_display():

    print('\n')
    print("-+" * 17)
    print(f"{HEAD_DISPLAY}")
    print("-+" * 17)
    print("-" * 80)

    print("-+" * 12)
    print("First 10 rows of the file")
    print("-+" * 12)
    print("-" * 80)

    # Open and only print rows within index 0 and 10
    with open(BAL_DATA, "r", newline='') as f:
        bal_read = csv.reader(f, delimiter=',')
        for i, row in enumerate(bal_read):
            if i > 0 and i <= 10: 
                print(row)
                print("-" * 80)
            elif i > 10:
                break
        else:
            pass
    return


"""
Alphabetically Filtered Rows
"""
def field_specified():

    user_field_column = ''
    user_job_element = ''
    user_element_column = ''
    
    print('\n')
    print("--- first_name | job_title | balance ---")
    print("-" * 80)
    user_field_column = input("Enter a field name to display its contents or type 'quit' to exit: ").lower().strip()
    
    if user_field_column == 'quit':
        print("Exiting program...")
        time.sleep(0.7)
        return
    elif user_field_column == 'first_name':
         user_element_column = input("Enter a letter to filter names by: (i.e. 'A' or 'z'): ").upper().strip()
    elif user_field_column == 'job_title':
         user_job_element = input("Enter a letter to filter job titles by (i.e. 'A' or 'z'): ").upper().strip()
    else:
         user_field_column == 'balance'
    
    print("-" * 80)
    
    print("\n")

    if user_element_column or user_job_element:
        print("-+" * 15)
        print(f"Records are filtered by letter")
        print("-+" * 15)
        print("-" * 80)

    # Read and print contents of the user specified field 
    with open(BAL_DATA, 'r', newline='') as f:
        bal_read = csv.DictReader(f, delimiter = ',', fieldnames=HEAD)
        for row in bal_read:
            try:
                if user_field_column == NME:  
                    if row[NME].startswith(user_element_column):
                        print(row[NME])
                        print("-" * 80)
                elif user_field_column == JOB:   
                    if row[JOB].startswith(user_job_element):  
                        print(row[JOB])
                        print("-" * 80)
                elif user_field_column == BAL:            
                    print(row[BAL])
                    print("-" * 80)
                else:
                    pass
            except ValueError:
                print("NO VALID ENTRY - QUITTING PROGRAM")
                time.sleep(0.7)
                return
            
"""
Adding Records
"""
def record_append():
    print('\n')
    print("--- Adding and Displaying a Record ---")
    print("-" * 80)
    
    usr_append_name = input("Enter your first name: ")
    usr_append_job = input("Enter your occupation: ")
    usr_append_bal = input("Enter your current net worth ($xxx,xxx.xx): ")
    print("-" * 80)

    print('\n')
    print("-+" * 17)
    print(f"{HEAD_DISPLAY}")
    print("-+" * 17)
    print("-" * 80)

    record_list = [usr_append_name, usr_append_job, usr_append_bal] 

    # Append user values to a new row in the file
    with open(BAL_DATA, 'a', newline='') as f:
        f.write('\n')
        write_record = csv.writer(f, delimiter=',', lineterminator='\n')
        write_record.writerow(record_list)

    # Open and output the new rows along with a few of the proceeding rows
    with open(BAL_DATA, 'r', newline='') as f:
        bal_read = csv.reader(f)        
        for i, row in enumerate(bal_read):
                if i in ROW_RANGE and i:
                    print(','.join(row))
                    print("-" * 80)
    
"""
Modifying Records
"""
def record_modify():
    print('\n')
    print(" --- Modify a Record ---")
    print("-" * 80)
    usr_modify_name = input("Enter first name to modify the associated record: ") 
    print("-" * 80)

    print('\n')
    print("-+" * 17)
    print(f"{HEAD_DISPLAY}")
    print("-+" * 17)
    print("-" * 80)

    # Initialize a variable to read and row index variable
    all_rows = []
    record_found = False
    row_index = -1

    # Search through the CSV to find the user specified record
    with open(BAL_DATA, 'r', newline='') as f:
         bal_read = csv.reader(f, delimiter=',')
         for i, row in enumerate(bal_read):
              all_rows.append(row)
              if i > 0 and row[0].lower() == usr_modify_name.lower():
                record_found = True
                row_index = i
                # Display the found record
                print(f"Found record: {row}")
                print("-" * 80)

    if not record_found:
        print(f"Record with name '{usr_modify_name}' not found.")
        return
    
    print("\nFields available to modify: ")
    print("1: first_name")
    print("2: job_title")
    print("3: balance")
    # Asks which field to modify (first_name, job_title, or balance)
    field_choice = input("Enter the field number to modify (1-3): ").strip()
    
    # Verify the field to modify
    if field_choice == '1':
        new_value = input("Enter new first name: ").strip()
        all_rows[row_index][0] = new_value
    elif field_choice == '2':
        new_value = input("Enter new job title: ").strip()
        all_rows[row_index][1] = new_value
    elif field_choice == '3':
        new_value = input("Enter new balance ($xxx,xxx.xx): ").strip()
        all_rows[row_index][2] = new_value
    else:
        print("Invalid Choice")
        return 

    # Rewrites the entire CSV file with the updated record
    # WARNING: If the program crashes or abruptly fails during this segment the file could be left empty
    # Double check the CSV file if the program ends during this code block
    with open(BAL_DATA, 'w', newline='') as f:
        record_write = csv.writer(f, delimiter=',', lineterminator='\n')
        record_write.writerows(all_rows)

    print("-" * 80)
    print(f"Record updated succesfully")
    time.sleep(1)
    print(f"New record: {all_rows[row_index]}")
    print("-" * 80)

"""
MAIN MENU
"""
def main():
    print("-" * 80)
    print("1: Display the first 10 lines of the file")
    print("2: Display specific a specific record type and choose an element to filter")
    print("3: Add and display a new record")
    print("4. Modify an existing record")
    print("q: Exit")

    print("-" * 80)
    usr_mode_choice = input("Enter an index number to execute the associated action or type 'quit' to exit: ").strip()
    print("-" * 80)

    if usr_mode_choice.lower() == 'q':
        print("Exiting program...")
        time.sleep(0.7)
        return
    elif usr_mode_choice == '1':
        row_display()
    elif usr_mode_choice == '2':
        field_specified()
    elif usr_mode_choice == '3':
        record_append()
    elif usr_mode_choice == '4':
        record_modify()
    else:
        print("*INVALID INPUT*")
        print("Exiting program...")
        time
        return
    
if __name__ == '__main__':
    main()