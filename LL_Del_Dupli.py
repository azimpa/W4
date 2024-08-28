class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_duplicates(self):
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(30)
linked_list.insert(10)
linked_list.insert(50)
print("Original Linked List:")
linked_list.display()
linked_list.remove_duplicates()
print("Linked List after removing duplicates:")
linked_list.display()
