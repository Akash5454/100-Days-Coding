"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.

Time Complexity O(N)
"""

def isBST(root, min_, max_):

    if root is None:
        return True

    if(min_ != None and min_ >= root.val) or
    (max_ != None and max_ <= root.val):
        return False

    if (!isBST(root.left, min_, root.val) or !isBST(root.right, root.val, max_)):
        return False

    return True 
        
def main(root):
    return isBST(root, None, None)



