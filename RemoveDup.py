"""
Remove Duplicates: Write code to remove duplicates from an unsorted linked list.

Time Complexity O(n)
"""

def removeDup(head):
    if head == None:
        return head
    pre = None
    curr = head
    d = {} 
    while curr is not None:
        if curr.data not in d.keys():
            d[curr.data] = 1
            pre = curr
        else:
            pre.next = curr.next
        curr = curr.next
    return head
        
        
        
