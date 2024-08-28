class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("LL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, "-->", end=" ")
                current = current.next

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def add_after(self, data, x):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if x == current.data:
                break
            current = current.next
        if current is None:
            print("Node not presented in LL")
        else:
            new_node.next = current.next
            current.next = new_node

    def add_before(self, data, y):
        new_node = Node(data)
        if self.head.data == y:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            if current.next.data == y:
                break
            current = current.next
        if current.next is None:
            print("value not found")
        else:
            new_node.next = current.next
            current.next = new_node

    # <-----------------------------------------------------------deletion------------------------------------------------------------------------------------->

    def del_begin(self):
        if self.head is None:
            print("LL is empty, can't delete")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("LL is empty, can't delete")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None

    def del_any(self, d):
        if self.head is None:
            print("LL is empty,can't delete")
        elif d == self.head.data:
            if self.head.next is None:
                self.head = None
                print("LL is empty after deletion")
            else:
                self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if d == current.next.data:
                    break
                current = current.next
            if current.next is None:
                print("Node not found")
            else:
                current.next = current.next.next


link = LL()
link.add_begin(4)
link.add_begin(3)
link.add_begin(1)
link.add_end(6)
link.add_end(7)
link.add_after(2, 7)
link.add_before(5, 1)
# link.del_begin()
# link.del_end()
# link.del_any(7)
link.print_ll()
