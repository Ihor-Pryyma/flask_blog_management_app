class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def __custom_hash(self, key: str) -> int:
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.__custom_hash(key)
        new_node = Node(Data(key, value), None)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = new_node
        else:
            node = self.hash_table[hashed_key]
            while node.next:
                node = node.next
            node.next = new_node

    def get_value(self, key):
        hashed_key = self.__custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            while node:
                if node.data.key == key:
                    return node.data.value
                node = node.next
        return None

    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next:
                    while node.next:
                        llist_string += (str(node.data.key) + " : " + str(node.data.value) + " -->")
                        node = node.next
                        llist_string += (str(node.data.key) + " : " + str(node.data.value) + " --> None")
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")
