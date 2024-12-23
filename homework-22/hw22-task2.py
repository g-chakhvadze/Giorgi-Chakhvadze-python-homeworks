class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, element):
        self.queue.append(element)

    def pop(self):
        if not self.queue:
            raise IndexError("pop from empty queue")
        return self.queue.pop(0)

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
print(q.pop())
print(q.pop())
print(q.pop())
