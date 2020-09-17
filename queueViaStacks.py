"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

Time Complexity O(1)
"""

class Queue:

    def __init__(self, capacity):
        self.s1 = []
        self.s2 = []
        self.capacity = capacity

    def push(self, item):
        if self.isFull():
            raise Exception('Queue Overflow')
        if len(self.s1) == 0:
            self.front = item
        self.s1.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception('Queue Underflow')
        if len(self.s2) == 0:
            while(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2.pop()        
        

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue Underflow')
        if len(self.s2) != 0:
            return self.s2[-1]
        else:
            return self.front

    def isFull(self):
        return len(self.s1) == self.capacity

    def isEmpty(self):
        return len(self.s1)==0 and len(self.s2)==0
