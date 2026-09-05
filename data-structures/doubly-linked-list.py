class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None
        self.prev = None

if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(10)
    n3 = Node(2)
    n4 = Node(7)

    head = n3
    tail = n2

    n3.next = n1
    n1.prev = n3

    n1.next = n4
    n4.prev = n1

    n4.next = n2
    n2.prev = n4

    print("Traverse forward")
    curr = head
    while curr != None:
        print(curr.value, end=" -> ")
        curr = curr.next

    print("\nTraverse backwards")
    curr = tail
    while curr != None:
        print(curr.value, end=" -> ")
        curr = curr.prev