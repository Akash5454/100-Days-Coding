"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

"""
import sys

class Stack:

    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.array = [-1]*self.stacksize
        self.top = -1

    def push(self, item):
        if self.isFull():
            raise Exception('Stack is Full')
        self.top += 1
        self.array[self.top] = item

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        val = self.array[self.top]  
        self.array[self.top] = -1
        self.top -= 1
        return val

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        return self.array[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.stacksize - 1

    def sortStack(self):
        tempStack = []
        tempStack.append(self.pop())
        while not self.isEmpty():
            temp = self.pop()
            while(len(tempStack) != 0) and temp<=tempStack[-1]:
                self.push(tempStack.pop())
            tempStack.append(temp)
        return tempStack
        
            
stack = Stack(5)
stack.push(4)
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(5)
print(stack.sortStack())

