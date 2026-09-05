class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None

if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(10)
    n3 = Node(2)
    n4 = Node(7)

    n3.next = n1
    n1.next = n4
    n4.next = n2

    print("Traverse forward")
    curr = n3
    while curr != None:
        print(curr.value, end=" -> ")
        curr = curr.next