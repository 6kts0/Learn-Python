import csv
import time

BAL_DATA = "balanceCorrelation.csv"
ROWS_10 = 10
HEAD_DISPLAY = ['Name' ' | ' 'Occupation' ' | ' 'Net Worth']
HEAD = ['first_name', 'job_title', 'balance']
# -------------------------------------------------- # 
NME = 'first_name'
JOB = 'job_title'
BAL = 'balance'

USR_RECORD_NEW = []

# Display first 10 rows
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


# Display a specific fields with alphabetic filtering
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
    print("-+" * 17)
    print(f"{HEAD_DISPLAY}")
    print("-+" * 17)
    print("-" * 80)

    if user_element_column or user_job_element:
        print("-+" * 15)
        print(f"Records are filtered by letter")
        print("-+" * 15)
        print("-" * 80)


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
    return

def main():
    print("1: Display the first 10 lines of the file")
    print("2: Display specific records and choose elements to filter")
    print("3: Add a new record")
    print("4. Modify an existing record in any of the three categories")

    usr_mode_choice = input("Enter an index number to execute the associated action: ")

    if usr_mode_choice == '1':
        row_display()
    elif usr_mode_choice == '2':
         field_specified()
    else:
        print("No input found")
        print("Returning to menu...")
        return
    
if __name__ == '__main__':
     main()