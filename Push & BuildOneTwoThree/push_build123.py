'''PUSH & BUILD 123'''
class Node:
    '''class to store info about nods'''
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    '''push a node into a linked list'''
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    '''build a linked list by 1 -> 2 -> 3 -> None'''
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    return one
