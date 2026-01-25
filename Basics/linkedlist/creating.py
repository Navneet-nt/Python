class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def traverse(self):
        current_node = self.head
        while current_node:
            print(f'{current_node.data} ->', end = " ")
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    linkedlist = Linkedlist()
    for i in range(5):
        linkedlist.append(i)
    linkedlist.traverse()