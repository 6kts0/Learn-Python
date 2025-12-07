import csv
import time

BAL_DATA = "balanceCorrelation.csv"
ROWS_10 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
HEADS = ['Name' ' | ' 'Occupation' ' | ' 'Net Worth']
# -------------------------------------------------- # 
NME = 'first_name'
JOB = 'job_title'
BAL = 'balance'

USR_RECORD_NEW = []


def row_display():

    print('\n')
    print("-+" * 17)
    print(f"{HEADS}")
    print("-+" * 17)

    print("-" * 80)
    with open(BAL_DATA, "r", newline='') as f:
        bal_read = csv.reader(f, delimiter=',')
        for i, row in enumerate(bal_read):
            if i in ROWS_10:
                print(row)
                print("-" * 80)
            else:
                pass
row_display()


def field_specified():
    print('\n')

    print("FIELDS: first_name | job_title | balance ")
    usr_choice_column = input("Enter a field to display or type 'quit' to exit: ").strip()

    sep = ","

    print("\n")
    print("-+" * 17)
    print(f"{HEADS}")
    print("-+" * 17)
    print("-" * 80)

    with open(BAL_DATA, 'r', newline='') as f:
        bal_read = csv.DictReader(f,) 
        for row in bal_read:
            if len(row[usr_choice_column]) > 0:
                try:
                    if usr_choice_column == NME:  
                        print(row[NME])
                        print("-" * 80)
                    elif usr_choice_column == JOB:
                        print(row[JOB])
                        print("-" * 80)
                    elif usr_choice_column == BAL:
                        print(''.join(list(row[BAL])))
                        print("-" * 80)
                    elif usr_choice_column.lower().strip() == 'quit':
                        print("Exiting program...")
                        time.sleep(0.7)
                        return
                    else:
                        print(row)
                except ValueError:
                    print("*INVALID ENTRY* Try again...")
            else:
                print("NO VALID ENTRY - QUITTING PROGRAM")
                time.sleep(0.7)
                return



field_specified()

def main():
    print("1: Display the first 10 lines of the file")
    print("2: Display net worths from greatest to least")
    print("3: Add a new record")
    print("4. Modify an existing record in any of the three categories")

    usr_mode_choice = input("Enter an index number to execute the associated action: ")
