class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert_recursive(self, node, data):
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__insert_recursive(node.left, data)
        elif data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__insert_recursive(node.right, data)
        else:
            return

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert_recursive(self.root, data)

    def __search_recursive(self, node, blog_post_id):
        if blog_post_id == node.data['id']:
            return node.data
        if blog_post_id < node.data['id'] and node.left is not None:
            if blog_post_id == node.left.data['id']:
                return node.left.data
            return self.__search_recursive(node.left, blog_post_id)
        if blog_post_id > node.data['id'] and node.right is not None:
            if blog_post_id == node.right.data['id']:
                return node.right.data
            return self.__search_recursive(node.right, blog_post_id)
        return False

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self.__search_recursive(self.root, blog_post_id)
