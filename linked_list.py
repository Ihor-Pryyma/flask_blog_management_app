class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_ll(self):
        ll = ""
        node = self.head
        while node:
            ll += f"{node.data!r} -> "
            node = node.next
        ll += "None"
        print(ll)

    def insert_beginning(self, value):
        new_node = Node(value, self.head)
        if self.tail is None:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, value):
        if self.head is None:
            return self.insert_beginning(value)

        new_node = Node(value, None)
        self.tail.next = new_node
        self.tail = new_node

    def to_list(self):
        l = []
        if self.head:
            temp = self.head
            while temp:
                l.append(temp.data)
                temp = temp.next
        return l

    def get_user_by_id(self, user_id):
        temp = self.head
        while temp:
            if temp.data["id"] == int(user_id):
                return temp.data
            temp = temp.next
