"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

Time Complexity O(M+N)
"""

def intersect(head1, head2):
    if head1 is None or head2 is None:
        return None
    length1 = 0
    length2 = 0
    ptr1 = head1
    ptr2 = head2
    while ptr1 is not None:
        ptr1 = ptr1.next
        length1 += 1
    while ptr2 is not None:
        ptr2 = ptr2.next
        length2 += 1
    ptr1 = head1
    ptr2 = head2
    diff = abs(length1-length2)
    if length1 >= length2:
        while diff:
            ptr1 = ptr1.next
            diff -= 1
        while ptr1 is not None and ptr2 is not None:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return None
    else:
        while diff:
            ptr2 = ptr2.next
            diff -= 1
        while ptr1 is not None and ptr2 is not None:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return None
