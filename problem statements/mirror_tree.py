class TreeNode:
    def __init__(self, x):  
        self.value = x
        self.left = None
        self.right = None

def insert_node(nodes, u, v, c):
    if u not in nodes:
        nodes[u] = TreeNode(u)
    if v not in nodes:
        nodes[v] = TreeNode(v)

    if c == 'L':
        nodes[u].left = nodes[v]
    else:
        nodes[u].right = nodes[v]

def are_mirrors(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.value != t2.value:  
        return False
    return are_mirrors(t1.left, t2.right) and are_mirrors(t1.right, t2.left)


tree1 = {}
insert_node(tree1, 1, 2, 'L')
insert_node(tree1, 1, 3, 'R')

tree2 = {}
insert_node(tree2, 1, 2, 'R')
insert_node(tree2, 1, 3, 'L')

root1 = tree1[1]
root2 = tree2[1]


print("yes" if are_mirrors(root1, root2) else "no")
