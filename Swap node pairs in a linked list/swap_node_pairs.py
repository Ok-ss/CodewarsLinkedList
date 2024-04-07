class Node:
    def __init__(self, next=None):
        self.next = next
    
def swap_pairs(head:Node):
    node = head
    prev = None
    while node and node.next:
        nxt_node = node.next
        rest = nxt_node.next
        node.next = rest
        nxt_node.next = node
        if prev:
            prev.next = nxt_node
        if node == head:
            head = nxt_node
        prev = node
        node = rest
        
    return head
