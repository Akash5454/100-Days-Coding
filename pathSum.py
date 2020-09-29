"""
Path Sum: Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

"""

def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    sum = sum - root.val
    if not root.left and not root.right:
        return sum == 0
    else:
        return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)
            
        
