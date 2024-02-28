class binary_search_tree:
    """
    A binary search tree data structure.
    """
    def __init__(self, *args):
        self.root = node(args[0])

        for value in list(args)[1:]:
            self.insert(value)

    def __str__(self, node = None, level = 0):
        node = self.root if node is None else node
        string = '' if node.right is None else self.__str__(node.right, level + 1)
        string += '\t' * level + str(node) + '\n'
        string += '' if node.left is None else self.__str__(node.left, level + 1)
        return string

    def minimum(self):
        return self.root.minimum()

    def maximum(self):
        return self.root.maximum()

    def search(self, key):
        return self.root.search(key)

    def insert(self, key):
        if self.search(key) is not None:
            return

        node = self.root

        while 1:
            if node.key <= key:
                if node.right is None:
                    node.add_right(key)
                    break
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.add_left(key)
                    break
                else:
                    node = node.left

    def remove(self, key):
        node = self.search(key)

        if node.right is None:
            self.substitute(node, node.left)
        elif node.left is None:
            self.substitute(node, node.right)
        else: 
            key = node.successor().key
            self.remove(key)
            node.key = key

    def substitute(self, old, new):
        if old.is_root():
            self.root = new
        else:
            if old.is_right_child():
                old.parent.right = new
            else:
                old.parent.left = new


class node:
    """
    A node of a binary search tree.
    """
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None

    def __str__(self):
        return f'({self.key})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.key})'

    def is_root(self):
        return self.parent is None

    def is_right_child(self):
        return not self.is_root() and self.parent.right is self

    def add_right(self, key):
        self.right = node(key)
        self.right.parent = self

    def add_left(self, key):
        self.left = node(key)
        self.left.parent = self

    def minimum(self):
        node = self

        while node.left is not None:
            node = node.left

        return node

    def maximum(self):
        node = self

        while node.right is not None:
            node = node.right

        return node

    def successor(self):
        if self.right is None:
            node = self

            while not node.parent.is_root() and node.is_right_child():
                node = node.parent

            return node.parent
        else:
            return self.right.minimum()

    def search(self, value):
        node = self

        while node is not None:
            if node.key == value:
                return node
            elif node.key < value:
                node = node.right
            else:
                node = node.left

        return None


if __name__ == "__main__":
    tree = binary_search_tree(3, 2, 0, 1, 6, 4, 7, 5, 9)
    tree.remove(3)

    print('The minimum of the tree is', tree.minimum())
    print('The maximum of the tree is', tree.maximum())
    print('\n', tree)

