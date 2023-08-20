class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next
        removed.next = None
        return removed
