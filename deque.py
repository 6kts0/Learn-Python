"""
Deque
All operations fail if deque is empty
"""

from collections import deque

# Regular list
l = [1, 2, 3, 4, 5]
print(l)


# Initialize deque list
L = deque([1, 2, 3, 4, 5])
L.appendleft(0) # Append item to leftmost side
print(L)

# Pop item in deque
pop_item = L.pop()
appendR = (5, 6) # Initialize tuple
L.append(appendR) # Append tuple to right most side of deque
print(L)