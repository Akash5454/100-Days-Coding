"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

"""

def leftMost(root):
    if root == None:
        return None
    while root.left is not None:
        root = root.left
    return root

def successor(root):
    if root is None:
        return None
    if root.right:
        return leftMost(root.right)
    else:
        q = root
        x = q.parent
        while (x is not None) and (x.left is not q):
            q = x
            x = x.parent
        return x
