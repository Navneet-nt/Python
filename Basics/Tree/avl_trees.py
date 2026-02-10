class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return str(self.value)

class AVLTree:
    def __init__(self):
        self.root = None

    def getheight(self, node):
        if node is None:
            return 0
        return node.height

    def getbalance(self, node):
        if node is None:
            return 0
        return self.getheight(node.left) - self.getheight(node.right)

    def right_rotate(self, node):
        x = node.left
        y = x.right
        x.right = node
        node.left = y

        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))
        x.height = 1 + max(self.getheight(x.left), self.getheight(x.right))

        return x

    def left_rotate(self, node):
        x = node.right
        y = x.left
        x.left = node
        node.right = y

        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))
        x.height = 1 + max(self.getheight(x.left), self.getheight(x.right))

        return x

    def insert(self, root, value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))

        balance = self.getbalance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def preOrder(self, root):
        if not root:
            return
        print(f"{root.value} ", end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


if __name__ == "__main__":
    tree = AVLTree()
    root = None

    # Let's insert sorted numbers that would normally break a BST
    numbers = [10, 20, 30, 40, 50, 25]

    print("Inserting nodes...")
    for num in numbers:
        root = tree.insert(root, num)

    print("\nPreorder traversal of constructed AVL tree is:")
    tree.preOrder(root)


