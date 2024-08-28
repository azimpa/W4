class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, "-->", end=" ")
            current = current.next
        print()


array = [1, 2, 3, 4, 5, 6]
l1 = Linkedlist()
for data in array:
    l1.add_node(data)
l1.display()
