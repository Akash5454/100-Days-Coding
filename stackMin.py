"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

"""
import sys

class Stack:

    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.array = [-1]*self.stacksize
        self.min_arr = [sys.maxsize]*self.stacksize
        self.top = -1

    def push(self, item):
        if self.isFull():
            raise Exception('Stack is Full')
        
        if self.min_arr[self.top]>item:
            self.top += 1
            self.min_arr[self.top] = item
        else:
            self.top += 1
            self.min_arr[self.top] = self.min_arr[self.top-1]
        self.array[self.top] = item

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        val = self.array[self.top]  
        self.array[self.top] = -1
        self.min_arr[self.top] = sys.maxsize 
        self.top -= 1
        return val

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        return self.array[self.top]

    def stackMin(self):
        
        return self.min_arr[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.stacksize - 1

def stackMin():
    stack = Stack(5)
    print(stack.isEmpty())
    stack.push(3)
    print(stack.isEmpty())
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(9)
    print(stack.isFull())
    print(stack.stackMin())
    stack.pop()
    stack.pop()
    print(stack.stackMin())
    
if __name__ == '__main__':
    stackMin()
