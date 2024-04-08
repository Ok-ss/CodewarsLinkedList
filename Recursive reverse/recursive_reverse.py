'''REVERSE RECURSIVELY'''
class Node(object):
    '''class to store info about nods'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head:Node):
    '''reverse a linked list recursively'''
    if head:
        prev = None
        node = head
        if not head.next:
            return head
        while node.next:
            prev = node
            node = node.next
        prev.next = None
        node.next = reverse(head)
        return node
    return None
