class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        self.internalArray.append(item)

        # Code to add an item to the stack will go here

    def pop(self):
        if len(self.internalArray) == 0:
            print("Stack is empty")
        else:
            lastitem = self.internalArray[-1]
            del self.internalArray[-1]
            print(lastitem)

    def peek(self):
        lastitem = self.internalArray[-1]
        print(lastitem)

    def __str__(self):
        return self.internalArray.__str__()


stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)
print(stack1)
popped1 = stack1.pop()
popped2 = stack1.pop()
peeked1 = stack1.peek()
peeked2 = stack1.peek()
stack2 = Stack()
stack2.push("Linx")
stack2.push("Windows")
stack2.push("Max OS X")
print(stack2)
popped3 = stack2.pop()
popped4 = stack2.pop()
popped5 = stack2.pop()
popped6 = stack2.pop()
