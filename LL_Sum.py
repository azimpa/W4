class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("LL is Empty") 
        else:
            current = self.head
            while current is not None:
                print(current.data,"-->",end=" ")
                current=current.next

    def print_sum(self):
        sum = 0
        current = self.head
        while current is not None:
            sum = sum + current.data
            current = current.next
        print(sum)        

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node       
    
LL1=LinkedList()
LL1.append(11)
LL1.append(21)
LL1.append(31)
LL1.append(41)
LL1.print_ll()
LL1.print_sum()
