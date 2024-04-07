class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head:
        node = head
        prev = Node(0)
        while node:
            if node.data != prev.data:
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = prev.next
        return head
        
    return None

