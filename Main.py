import os
class Stack:
    """The class implements a Stack ADT using a list object
    Attributes:
        items: a list functioning as a stack to hold data
        size: an int storing the maximum size of the stack"""
    
    def __init__(self, size):
        """Initialises the object with attributes items and size"""
        self.items = []
        self.size = size

    def is_empty(self):
        """Returns True if the stack is empty, False if not"""
        return len(self.items) == 0

    def is_full(self):
        """Returns True if the stack is full, False if it is not"""
        return len(self.items) == self.size

    def push(self, data):
        """Takes argument 'data'. Pushes the provided data into the stack, if it is not full"""
        if not self.is_full():
            self.items.append(data)

    def pop(self):
        """Removes the top element of the stack, if it exists"""
        if not self.is_empty():
            self.items.pop(-1)

    def status(self):
        """Prints each element of the stack on a separate line"""
        for element in stack.items:
            print(element)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
