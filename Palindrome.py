"""
Palindrome: Implement a function to check if a linked list is a palindrome.

Time Complexity O(n)
"""

def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    return prev

def isPalindrome(head):
    count = 0
    if head is None:
        return True
    ptr = head
    while ptr is not None:
        ptr = ptr.next
        count += 1
    if count%2 == 0:
        mid = count//2
    else:
        mid = (count//2) + 1
    ptr = head
    while mid:
        ptr = ptr.next
        mid -= 1
    head2 = reverse(ptr)
    temp2 = head2
    temp1 = head
    while temp1 is not None and temp2 is not None:
        if temp1.data != temp2.data:
            return False
        temp1 = temp1.next
        temp2 = temp2.next
    return True
