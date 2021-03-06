#implementing stack using dequeue
from collections import  deque
class Stack:
    def __init__(self):
        self.items = deque()

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0