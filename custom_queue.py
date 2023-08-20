class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head is None and self.tail is None:
            self.tail = self.head = Node(data)
            return
        self.tail.next = Node(data)
        self.tail = self.tail.next
        return

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        removed.next = None
        return removed
