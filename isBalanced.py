"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

"""

"""
Method 1

Time Complexity O(NlogN)
"""

def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1

def isBalanced(root):
    if root is None:
        return -1
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    if abs(leftHeight-rightHeight) > 1:
        return False
    else:
        return isBalanced(root.left) and isBalanced(root.right)

"""
Method 2

Time Complexity O(N)
"""
import sys

min_ = -sys.maxsize-1

def height(root):
    
    if root is None:
        return -1
    leftHeight = height(root.left)
    if leftHeight == min_:
        return min_
    rightHeight = height(root.right)
    if rightHeight == min_:
        return min_
    if abs(leftHeight-rightHeight)>1:
        return min_
    else:
        return max(leftHeight, rightHeight) + 1

def isBalanced(root):
    return height(root) != min_ 
    
