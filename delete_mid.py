"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

Time Complexity O(n)
"""

def del_mid(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    pre = None
    while fast is not None fast.next is not None:
        fast = fast.next.next
        pre = slow
        slow = slow.next
    pre.next = slow.next
    return head
