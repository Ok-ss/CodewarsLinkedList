'''MODULE THAT TURNS LINKED LIST INT A STRING'''
class Node:
    '''class to store info about nods'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node 

def stringify(node:Node):
    '''function to turn linked list into string'''
    res = ''
    while node is not None:
        res += f'{node.data} -> '
        node = node.next
    return res + 'None'
