"""
Three in One: Describe how you could use a single array to implement three stacks.

"""

class MultiStacks:

    def __init__(self, numstacks, stacksize):
        self.numstacks = numstacks
        self.stacksize = stacksize
        self.array = [0]*(self.numstacks*self.stacksize)
        self.size = [0]*(numstacks)

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception('Stack is Full')
        self.size[stacknum] += 1
        self.array[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is Empty')
        val = self.array[self.indexOfTop(stacknum)]
        self.array[self.indexOfTop(stacknum)] = 0
        self.size[stacknum] -= 1
        return val

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is Empty')
        return self.array[self.indexOfTop(stacknum)]

    def isFull(self, stacknum):
        return self.size[stacknum] == self.stacksize

    def isEmpty(self, stacknum):
        return self.size[stacknum] == 0

    def indexOfTop(self, stacknum):
        offset = stacknum*self.stacksize
        return offset + self.size[stacknum] - 1

def threeInOne():
    stack = MultiStacks(3,3)
    print(stack.isEmpty(1))
    stack.push(3, 1)
    print(stack.peek(1))
    print(stack.isEmpty(1))
    stack.push(2, 1)
    print(stack.peek(1))
    print(stack.pop(1))
    print(stack.peek(1))
    stack.push(3, 1)

if __name__ == '__main__':
    threeInOne()
    
    
    
