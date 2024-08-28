class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
array = linked_list_to_array(head)
print("array", array)