class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, keys=None, values=None, root_key=None, root_value=None):
        self.root = None
        self._size = 0

        if keys is not None and values is not None:
            for key, value in zip(keys, values):
                self.insert(key, value)
        elif root_key is not None and root_value is not None:
            self.insert(root_key, root_value)

    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
            self._size += 1
            return True
        else:
            return self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if key == node.key:
            return False
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
                self._size += 1
                return True
            else:
                return self._insert_recursive(node.left, key, value)
        else:
            if node.right is None:
                node.right = TreeNode(key, value)
                self._size += 1
                return True
            else:
                return self._insert_recursive(node.right, key, value)

    def contains(self, key):
        return self._contains_recursive(self.root, key)

    def _contains_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._contains_recursive(node.left, key)
        else:
            return self._contains_recursive(node.right, key)

    def remove(self, key):
        self.root, removed = self._remove_recursive(self.root, key)
        if removed:
            self._size -= 1
        return removed

    def _remove_recursive(self, node, key):
        if node is None:
            return node, False

        if key < node.key:
            node.left, removed = self._remove_recursive(node.left, key)
            return node, removed
        elif key > node.key:
            node.right, removed = self._remove_recursive(node.right, key)
            return node, removed
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                successor = self._find_min(node.right)
                node.key, node.value = successor.key, successor.value
                node.right, _ = self._remove_recursive(node.right, successor.key)
                return node, True

    def update(self, key, value):
        node = self._find(self.root, key)
        if node is not None:
            node.value = value
            return True
        else:
            return False

    def _find(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def print(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append((node.key, node.value))
            self._in_order_traversal(node.right, result)

    def size(self):
        return self._size

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    def max(self):
        node = self._find_max(self.root)
        return (node.key, node.value) if node else None

    def _find_max(self, node):
        while node and node.right:
            node = node.right
        return node

    def min(self):
        node = self._find_min(self.root)
        return (node.key, node.value) if node else None

    def _find_min(self, node):
        while node and node.left:
            node = node.left
        return node

    def lower_bound(self, key):
        result = None
        node = self.root
        while node:
            if node.key < key:
                result = (node.key, node.value)
                node = node.right
            else:
                node = node.left
        return result

    def upper_bound(self, key):
        result = None
        node = self.root
        while node:
            if node.key <= key:
                result = (node.key, node.value)
                node = node.right
            else:
                node = node.left
        return result