class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


# Define root and branch nodes
A = TreeNode(1)
B = TreeNode(4)
C = TreeNode(5)
D = TreeNode(8)
E = TreeNode(13)
F = TreeNode(22)
G = TreeNode(55)
H = TreeNode(91)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
D.left = H

def pre_order(node):
    if not node:
        return node
  
    print(node)
    pre_order(node.left)
    pre_order(node.right)


def main():
    pre_order(A)

if __name__ == '__main__':
    main()
