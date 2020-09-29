"""
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine ifT2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

Time Complexity O(nm)
"""

def isSubtree(s, t):
    def equals(root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        return root1.val == root2.val and equals(root1.left, root2.left) and equals(root1.right,root2.right)
            
    def traverse(s, t):
        return s is not None and (equals(s,t) or traverse(s.left,t) or traverse(s.right,t))
            
    return traverse(s,t)
