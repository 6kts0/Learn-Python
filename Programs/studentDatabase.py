import pandas as pd
from datetime import datetime
import os
import time


 
STUDENT_DATA = 'student_data.csv'
COLUMNS = ['Student ID', 'Name', 'Date of Birth', 'Grade']


"""
SAFETY FUNCTION
"""
# Load student data from csv or create new empty dataframe
def initialize_dataframe():
    if os.path.exists(STUDENT_DATA) and os.path.getsize(STUDENT_DATA) > 0:
        # Load student data file and confirm columns exist
        student_ppi = pd.read_csv(STUDENT_DATA)
        student_ppi['Student ID'] = student_ppi['Student ID'].astype(str) # Convert student ID to string to prevent type errors
        return student_ppi
    else:
        return pd.DataFrame(columns=COLUMNS) # Creates a new dataframe with predefined columns from COLUMNS


"""
ADDING RECORDS
"""
def add_student_data():
    
    # Loads existing csv or creates a new one and loads it
    student_ppi = initialize_dataframe()

    print("-+" * 30)
    print(" | ".join(COLUMNS))
    print("-+" * 30)

    while True:

        # Input student ID and print once entered
        student_id = input("Enter your student ID (or 'q' to return to menu): ").strip()

        # If user inputs 'q' return to main()
        if student_id.lower() == 'q':    
            return

        if student_id in student_ppi['Student ID'].values:
            print(f"*ERROR* {student_id} Already exists. Please enter a unique ID.")
            print("-" * 60)
            continue
        print(f"Student ID: {student_id}")
        print("-" * 60)

        # Input name print once entered
        name = (input("Enter your last name: "))
        print(f"Last name: {name}")
        print("-" * 60)

        # Check DOB formatting and force datetime format
        # Return error and force re-input if formatting error occurs
        while True:
            input_dob = input("Enter your date of birth (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(input_dob, '%Y-%m-%d') # Validate date formatting
                dob = input_dob
                break
            except ValueError:
                print(f"Invalid format. Pleae use YYYY-MM-DD.")
        print(f"Date of Birth: {dob}")
        print("-" * 60)
        

        while True:
            try:
                grade = int(input("Enter your grade level (1-20): "))
                if 1 <= grade <=20:
                    break
                else:
                    print("Grade level must be a number between 1 and 20. Please try again.")
            except ValueError:
                    print("*INVALID INPUT* Grade level must be a whole number between 1 and 20.")

        print(f"Current Grade/Year: {grade}")
        print("-" * 60)

        new_row = {"Student ID":student_id, "Name":name, "Date of Birth":dob, "Grade":grade}
        new_df_row = pd.DataFrame([new_row])
        
        # Add new row to the dataframe with pd.concat
        student_ppi = pd.concat([student_ppi, new_df_row], ignore_index=True)
        
        # Stores dataframe as csv
        student_ppi.to_csv(STUDENT_DATA, index=False)  
        
        # Print updated csv
        print("\n             --- Updated Records ---")
        print(pd.read_csv(STUDENT_DATA)) 
        print("-" * 60)


"""
MODIFYING RECORDS
"""
def modify_student_data():

    # Load existing csv containing student data
    student_ppi = initialize_dataframe()

    # If no data is found in student_data.csv user returns to main() function 
    if student_ppi.empty:
        print("No student data available. Add student records first.")
        return

    print("-+" * 30)
    print(" | ".join(COLUMNS))
    print("-+" * 30)

    while True:

        # Retrieve student ID to modify records belonging to said ID
        modify_id = input("Enter your Student ID to modify records (or 'q' to return to menu): ").strip()
        
        if modify_id.lower() == 'q':
            return
        
        print(f"Student ID: {modify_id}")
        print('-' * 60)

        # Verify student exists
        if modify_id not in student_ppi['Student ID'].values:
            print(f"Student ID {modify_id} does not exist. Please verify your ID number and try again.")
            print('-' * 60)
            continue
        
        # Initialize the modify column to None
        modify_column = None

        # Verify column to be modified
        valid_columns = ['Name', 'Date of Birth', 'Grade']
        print(f"Modifiable Records: {' | '.join(valid_columns)}") # Prints columns in a single line seperated by a vertical bar
        print('-' * 60)
        modify_column = input("Which record type would you like to edit: ").strip()
        print('-' * 60)

        column_to_update = None

        # Find column that matches input
        for col in valid_columns:
            if modify_column.lower() == col.lower() or modify_column.lower() == col.lower().replace(' ', ''):
                column_to_update = col
                break
        
        # Chekc for valid column input
        if modify_column is None:
            print ("*RECORD NOT FOUND* Please enter a valid record type.")
            print('-' * 60)
            continue

        # Input new record value
        new_record = input(f"Enter the new {column_to_update} information: ")
        print('-' * 60)

        # Validate DOB input formatting
        if column_to_update == "Date of Birth":
            try:
                datetime.strptime(new_record, '%Y-%m-%d')
            except ValueError:
                print("Invalid formatting. Please use YYYY-MM-DD. Update failed.")
                continue
            print('-' * 60)
        # New record input error handling and type conversion to str
        elif column_to_update == 'Grade':
            try:
                new_record = int(new_record) # Convert grade metric to an integer
            except ValueError:
                print("Grade must be a whole number. Update failed.")
                continue
            print('-' * 60)

        try:
            # Modify dataframe columns and values with .loc 
            student_ppi.loc[student_ppi['Student ID'] == modify_id, column_to_update] = new_record
            print("Modification successful!")
            print('-' * 60)

            # Save as updated csv
            student_ppi.to_csv(STUDENT_DATA, index=False)
        except Exception as e:
            print(f"*ERROR OCCURED* Update failed. Error details: {e}")
            continue
        
        # Print updated csv
        print("\n             --- Updated Records ---")
        print(pd.read_csv(STUDENT_DATA))   
        print("-" * 60) 


"""
DELETING RECORDS
"""
def delete_student_data():

    # Load existing csv containing student data
    student_ppi = initialize_dataframe()

    if student_ppi.empty:
        print("No student data available. Add student records first.")
        return

    print("-+" * 30)
    print(" | ".join(COLUMNS))
    print("-+" * 30)

    while True:

        # Retrieve student ID to delete associated records
        delete_id = input("Enter your Student ID to delete records (or 'q' to return to menu): ").strip()
        if delete_id.lower() == 'q':
            return
        
        print(f"Student ID: {delete_id}")
        print('-' * 60)
        
        # Verify student exists
        if delete_id not in student_ppi['Student ID'].values:
            print(f"Student ID {delete_id} does not exist. Please verify your ID number and try again.")
            print('-' * 60)
            continue
        
        try:
            # Confirm record deletion
            verify_deletion = input(f"Type 'yes' to delete the record associated with {delete_id} or press ENTER to exit: ").strip()
            if verify_deletion.lower() == 'yes':
                student_ppi = student_ppi[student_ppi['Student ID'] != delete_id]
                print("-" * 60) 
                print("*RECORD DELETED*")
                print("-" * 60) 
            elif verify_deletion.lower() != 'yes':
                return
            
            # Write to csv 
            student_ppi.to_csv(STUDENT_DATA, index=False)
        except Exception as e:
            print(f"*ERROR OCCURED* Update failed. Error details: {e}")
            continue
        
        # Print updated csv
        print("\n             --- Updated Records ---")
        print(pd.read_csv(STUDENT_DATA))   
        print("-" * 60) 


"""
MAIN MENU
"""
def main():
    while True:
        print("\n--- Updated Records ---")
        print("1: Add Student Records")
        print("2: Modify Student Records")
        print("3: Delete Student")
        print("4: Student Records")
        print("5: EXIT")

        function_call = input(("select an option: ")).strip()
        if function_call == '1':
            add_student_data()
        elif function_call == '2':
            modify_student_data()
        elif function_call == '3':
            delete_student_data()
        elif function_call == '4':
            print("\n--- Updated Records ---")
            print('-' * 60)
            print(pd.read_csv(STUDENT_DATA))
            print('-' * 60)
            return
        elif function_call == '5':
            print("Exiting program...")
            time.sleep(1)
            return
        else:
            print("*Invalid selection*")
            return

# Standard way to declare main()     
if __name__ == "__main__":
    main()