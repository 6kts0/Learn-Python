# Classes and Objects - University Employees 

class department():
     def __init__(self, deptID, name, location):
          self.deptID = deptID 
          self.name = name
          self.location = location

     def print_dept(self):
          print(self.deptID, self.name, self.location)


department1 = department(1, "CS", "Sciences")
department2 = department(2, "Marketing", "Business")
department3 = department(3, "History", "Humanities")
department4 = department(4, "Anatomy", "MedSciece")
department5 = department(5, "Physics", "Sciences")

print("=" * 100)
department1.print_dept()
department2.print_dept()
department3.print_dept()
department4.print_dept()
department5.print_dept()

class chairman():
     def __init__(self, eID, name, dob, salary, title, deptID):
          self.eID = eID
          self.name = name
          self.dob = dob
          self.salary = salary
          self.title = title
          self.deptID = deptID

     def print_chair(self):
          print(self.eID, self.name, self.dob, self.salary, self.title, self.deptID)

deptChair1 = chairman(111, "Linus Torvalds", "12/28/1969", "$168,233", "CS Department Chair", 1)
deptChair2 = chairman(222, "James Donaldson", "2/14/1998", "$144,106", "Marketing Department Chair", 2)
deptChair3 = chairman(333, "Carl Abbot", "10/03/1944", "$201,956", "History Department Chair", 3)
deptChair4 = chairman(444, "Richard Nathan", "4/05/2033", "$101,788", "Anatomy Department Chair", 4)
deptChair5 = chairman(555, "Isaac Newton", "7/22/1703", "$1,243,877", "Physics Department Chair", 5)

print("=" * 100)
deptChair1.print_chair()
deptChair2.print_chair()
deptChair3.print_chair()
deptChair4.print_chair()
deptChair5.print_chair()
print("=" * 100)