class Node:
    '''class to store info about nods'''
    def __init__(self, data):
        self.data = data
        self.next = None 

def push(head, data):
    # Your code goes here.
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    # Your code goes here.
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    return one

