'''GET LOOP LENTH'''
class Node:
    '''class to store info about nods'''
    def __init__(self, data):
        self.data = data
        self.next = None

def loop_size(node):
    '''get the size of the loop'''
    if node.next:
        node_1 = node
        node_2 = node
        node_1 = node_1.next
        node_2 = node_2.next.next
        strt_count = True
        counter = 0
        while node_1 != node_2 or strt_count:
            if node_1 == node_2:
                strt_count = False
            node_1 = node_1.next
            node_2 = node_2.next.next
            if not strt_count:
                counter += 1
        return counter
    raise Exception
