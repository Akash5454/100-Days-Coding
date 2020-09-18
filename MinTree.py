"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.

Time Complexity O(N)
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val == None:
            self.val = val
            return self.val
        else:
            if self.val > val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            else:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
                        
def MinTree(arr, start, end):
    if end < start:
        return None
    mid = (start+end)//2
    n = Node(arr[mid])
    n.left = MinTree(arr, start, mid-1)
    n.right = MinTree(arr, mid+1, end)
    return n
