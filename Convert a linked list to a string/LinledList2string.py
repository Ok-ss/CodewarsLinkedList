'''MODULE THAT TURNS LINKED LIST INT A STRING'''
class Node():
    '''Class to store node info'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    '''function to turn linked list into string'''
    res = ''
    while node is not None:
        res += f'{node.data} -> '
        node = node.next
    return res + 'None'
