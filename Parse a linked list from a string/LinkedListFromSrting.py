'''MODULE TO PARSE A LINKED LIST FROM A STRING'''

class Node:
    '''class to store info about nods'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self) -> str:
        return f'{self.data} -> {self.next}'

def linked_list_from_string(s):
    '''parse a linked list from string'''
    lst = s.split(' -> ')[:-1]
    head = None
    while len(lst) > 0:
        head = Node(lst[-1], head)
        lst.pop()
    return head# head to linked list
