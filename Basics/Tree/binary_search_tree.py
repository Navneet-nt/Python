class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class BST:

    def __init__(self):
        self.node = None

    def insert(self, value):
        if self.node is None:
            self.node = Node(value)
        else:
            self.insert_recursive(self.node, value)

    def insert_recursive(self, current_node, value):

        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert_recursive(current_node.left, value)

        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert_recursive(current_node.right, value)


def preorder(node):
    if node is not None:
        print(f"Node({node.value})")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(" / ")
        print(f"{node.value}", end="")
        print(" \ ")
        inorder(node.right)


if __name__ == "__main__":
    numbers = [10, 13, 2, 1, 5, 8, 0]
    tree = BST()
    for num in numbers:
        tree.insert(num)
    inorder(tree.node)
    tree = build(numbers)
    print(tree)
