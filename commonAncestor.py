"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.

Time Complexity O(N)
"""

def firstCommonAncestor(root, p, q):
    def traverse(node):
        if node == None:
            return False

        left = traverse(node.left)
        right = traverse(node.right)
        mid = node == p or node == q

        if mid + left + right >= 2:
            ans = node
        return mid or left or right
    traverse(root)
    return ans
