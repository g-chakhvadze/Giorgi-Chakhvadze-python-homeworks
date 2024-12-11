class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size()) 
