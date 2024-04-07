class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
    
    def __repr__(self) -> str:
        return f'{self.data} -> {self.next}'
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def __repr__(self) -> str:
        return f'{self.first}; {self.second}'
    
def alternating_split(head:Node):
    if head and head.next:
        node = head
        def append(head, new_node):
            if head:
                node = head
                while node.next:
                    node = node.next
                node.next = new_node
                return head
            return new_node
        first = None
        second = None
        while node:
            nxt_node = node.next
            node.next = None
            if nxt_node:
                rest = nxt_node.next
                nxt_node.next = None
            else:
                rest = None
            first = append(first, node)
            if nxt_node:
                second = append(second, nxt_node)
            node = rest
        return Context(first, second)


    raise Exception

F = Node('F', None)
E = Node('E', F)
D = Node('D', E)
C = Node('C', D)
B = Node('B', C)
A = Node('A', B)
print(alternating_split(A))