class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None

class BiDirectionalNode(Node):
    def __init__(self, value:int):
        super().__init__(value)
        self.prev = None
