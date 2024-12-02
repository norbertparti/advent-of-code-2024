class Node:
    def __init__(self, key, value):
        self.key = key
        self.values = [value]  # Store values in a list
        self.left = None
        self.right = None

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.insert(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.insert(key, value)
        else:
            # If key already exists, append the new value
            self.values.append(value)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root.insert(key, value)

    def find(self, key):
        return self._find_recursive(self.root, key)

    def _find_recursive(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.values  # Return all values for the key
        elif key < node.key:
            return self._find_recursive(node.left, key)
        else:
            return self._find_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            for value in node.values:  # Add all values for each key
                result.append((node.key, value))
            self._inorder_recursive(node.right, result)