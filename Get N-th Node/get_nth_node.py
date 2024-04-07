class Node:
    '''class to store info about nods'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node 

def get_nth(node, index):
    i = 0
    if not node:
        raise Exception
    while i != index:
        if not node.next:
            raise Exception
        node = node.next
        i+=1
    return node