'''SWAP PAIRS IN A LIST'''
class Node:
    '''class to store info about nods'''
    def __init__(self, nxt=None):
        self.next = nxt

def swap_pairs(head:Node):
    '''swap each pair in the linked list'''
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
