'''MOVE A NODE'''
class Node(object):
    '''class to store info about nods'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''class to store info about 2 linked list'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''move a node from one list to another'''
    if source:
        new_source = source.next
        source.next = dest
        return Context(new_source, source)
    raise Exception
