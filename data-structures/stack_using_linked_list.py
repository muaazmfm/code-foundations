from linked_lists.node import Node

class Stack:
    def __init__(self):
        self.head = None

    def pop(self):
        if not self.is_empty():
            popped = self.head
            self.head = self.head.next
            return popped.value
        return None

    def peak(self):
        if not self.is_empty():
            return self.head.value
        return None

    def is_empty(self):
        return self.head is None

    def push(self, i):
        new_node = Node(i)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node



if __name__ == "__main__":
    stack = Stack()

    for i in [1,2,3,4,5]:
        stack.push(i)

    print(stack.is_empty())
    print(stack.peak())
    print(stack.pop())
    print(stack.peak())
    print(stack.pop())
    stack.push(10)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
