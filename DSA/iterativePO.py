"""
Traversing Binary Trees
------------------------------
Iterative Pre Order Traversal
NODE > LEFT > RIGHT
"""

#    1
#  2   3
# 4  5  10
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# Iterative Pre Order Traversal
def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        print(node)

pre_order_iterative(A)