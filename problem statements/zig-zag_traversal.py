from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(n, edges):
    nodes = {}
    for u, v, c in edges:
        if u not in nodes:
            nodes[u] = Node(u)
        if v not in nodes:
            nodes[v] = Node(v)
        if c == 'L':
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]
    return nodes[edges[0][0]]  

def zigzag(root):
    if not root:
        return []

    q = deque([root])
    left_to_right = True
    result = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not left_to_right:
            level.reverse()
        result += level
        left_to_right = not left_to_right

    return result


n = int(input())
edges = [tuple(input().split()) for _ in range(n - 1)]

root = build_tree(n, edges)
print(*zigzag(root))
