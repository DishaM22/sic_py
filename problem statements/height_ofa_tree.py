class TreeNode:
    def __init__(self, x):
        self.x = x
        self.L = None  # left child
        self.R = None  # right child

def height(root):
    if root is None:
        return -1  # base case: empty node has height -1

    left = height(root.L)
    right = height(root.R)

    return 1 + max(left, right)

root = TreeNode(4)
root.L = TreeNode(2)
root.R = TreeNode(6)
root.L.L=TreeNode(1)
root.R .R= TreeNode(7)
print(height(root))
