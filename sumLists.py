"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

Time Complexity O(M+N)
"""

def add(head1, head2):
    carry, sum_ = 0,0
    temp = ListNode(-1)
    res = temp
    while head1 is not None or head2 is not None:
        if head1 is None:
            x = 0
        else:
            x = head1.data

        if head2 is None:
            y = 0
        else:
            y = head2.data

        sum_ = x + y + carry

        if sum_ >=10:
            carry = sum_//10
            sum_ = sum_%10
        else:
            carry = 0
    
        res.next = ListNode(sum_)

        if head1 is not None:
            head1 = head1.next
        if head2 is not None:
            head2 = head2.next

        res = res.next

        if carry>0:
            res.next = ListNode(carry)
            res = res.next
       return temp.next 
        
        
        
    
