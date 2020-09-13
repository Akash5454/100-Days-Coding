"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

Time Complexity O(n)
"""

def ret_kth(k, head):
    if head is None:
        return "Empty Linked list"
    ptr = head
    count = 0
    while ptr is not None:
        ptr = ptr.next
        count += 1
    if k>count:
        return "Length of the Linked list is smaller than Kth value"
    i = 0
    ptr = head
    while i < count-k:
        ptr = ptr.next
    return ptr.data
