#     __0__
#    /     \
#   2       5
#  / \     / \
# 3   1   6   4
"""
Recursive Post Order Traversal
LEFT > RIGHT > NODE
"""

class TreeNode():
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)

A = TreeNode(0)
B = TreeNode(2)
C = TreeNode(5)
D = TreeNode(3)
E = TreeNode(1)
F = TreeNode(6)
G = TreeNode(4)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)