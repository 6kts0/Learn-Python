"""
Python is a dynamically typed, object oriented programming language.
The value of a variable is a location in memory and the variable is a pointer.
The "del" statement can be used to unbind the reference to an object.
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Casting Values
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Implicit casting does not define the conversion of a value type
Explicit casting creates a new variable to hold the conversion of a value type
"""


# String Data Type
str_x = "25.5"

# Integer Data Type
int_x = 20

# Float Data Type
float_x = 20.5

# Complex Data Type
complex_x = 2j

# List Data Type
list_x = ["Apple", "Banana", "Mango"]

# Tuple Data Type
tuple_x = ("I", "Am", "LIST!")

# Range Data Type 
range_x = range(3)

# Dict Data Type
dict_x = {"name": "john", "age": "55", "bloodtype": "O-"}

# Set Data Type 
set_x = {"Apple", "Banana", "Mango"}

# Frozenset Data Type
frozenset_x = frozenset({"Apple", "Banana", "Mango"})

# Boolean Data Type
bool_x = True

# Bytes Data type
bytes_x  = b"Hello"

# Bytearray Data Type
bytearray_x = bytearray(5)

# Memoryview Data Type
memoryveiw_x = memoryview(bytes(5))

# None Data Type
none_x = None

# Printing data types
print(type(complex_x))
print(type(dict_x))

# Implicit casting integer to floating point
implicit_int = (int_x + float_x) 
print(implicit_int)

# Explicit casting tuple to list
explicit_list = list(tuple_x)
print(explicit_list)