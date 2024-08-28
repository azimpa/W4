class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None

    def print_dll(self):
        if self.head is None:
            print("DLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, "-->", end=" ")
                current = current.next
            print()

    def print_dll_rev(self):
        if self.head is None:
            print("DLL is empty")
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            while current is not None:
                print(current.data, "-->", end=" ")
                current = current.prev
            print()

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.prev = current

    def add_after(self, data, x):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if x == current.data:
                break
            current = current.next
        if current.next is None:
            if current.data == x:
                new_node.prev = current
                current.next = new_node
            else:
                print("given Node is note presented in DL")
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def add_before(self, data, x):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if x == current.data:
                break
            current = current.next
        if current.next is None:
            if x == current.data:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
            else:
                print("Node is note presented in DL")
        elif current.prev is None:
            new_node.next = current
            current.prev = new_node
            self.head = new_node
        else:
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.next = new_node

    # <-----------------------------------------------------------deletion------------------------------------------------------------------------------------->

    def del_begin(self):
        if self.head is None:
            print("DLL is empty,can't delete")
            return
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting")
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_end(self):
        if self.head is None:
            print("DLL is empty, can't delete")
            return
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deletion")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.prev.next = None

    def del_any(self, x):
        if self.head is None:
            print("DLL is empty,can't delete")
            return
        if self.head.next is None:
            if x == self.head.data:
                self.head = None
                print("DLL is empty after deletion")
            else:
                print("value not found")
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return

        current = self.head
        while current.next is not None:
            if x == current.data:
                break
            current = current.next
        if current.next is not None:
            current.next.prev = current.prev
            current.prev.next = current.next
        else:
            if x == current.data:
                current.prev.next = None
            else:
                print("x is not found in DLL")


DLL = Doubly()
DLL.add_begin(1)
DLL.add_end(3)
DLL.add_end(4)
DLL.add_end(6)
DLL.add_after(2, 1)
DLL.add_before(5, 6)
# DLL.del_begin()
# DLL.del_end()
# DLL.del_any(11)
DLL.print_dll()
# DLL.print_dll_rev()
