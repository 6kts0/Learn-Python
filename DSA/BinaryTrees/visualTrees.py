from binarytree import tree
import sys

# Generate random tree
my_tree = tree(height=4, is_perfect=True)

# Check the size and type before tree is converted to string type
print(type(my_tree))
print(f"Bytes: {sys.getsizeof(my_tree)}")

# Write tree to text file for visualization out of terminal
with open('tree.txt', 'w+') as f:
    f.write(str(my_tree))

