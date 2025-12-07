"""
--- Practice reading and writing to a csv file ---
read = 'r'
write = 'w'
read and write = 'r+' or 'w+'
Overwrite = 'w+'
Append = 'a'

--- This file is associated with prac.csv ---
"""

import csv
# Define header row / index[0]
HEADS = ["Name" ' | ' "Subject" ' | ' "Marks"]
MARK_WRITE = [["Faba", "Medical", 94.2]]
MARKS = [["Anita","Maths",83.0],
       ["Amar","Maths",95.0],
       ["Akash","Science",92.0],
       ["Ira","Science",99.0]]

# Initialized entry point to write to file
with open('prac.csv', 'w', newline='') as f:
    file_write = csv.writer(f, delimiter=';')

    print('-' * 80)
    # Write header names
    file_write.writerow(HEADS)
    
    # Write new data to a row
    for row in MARKS:
        file_write.writerow(row)

    # Write row to append
    for row in MARK_WRITE:
        file_write.writerow(row)

with open('prac.csv') as f:
    file_read = csv.reader(f, delimiter=';', dialect='excel')
    for row in file_read:
        print(row)
        print('-' * 80)
    
