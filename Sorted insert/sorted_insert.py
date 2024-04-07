class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head:Node, data):
    if head:
        to_insert = Node(data)
        if head.data > data:
            to_insert.next = head
            head = to_insert
        prev = head
        while prev.next and prev.next.data <= data:
            prev = prev.next
        next_node = prev.next
        prev.next = to_insert
        to_insert.next = next_node
        return head
    return Node(data)