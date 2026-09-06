from node import BiDirectionalNode, Node
from base import LinkedList

class DoublyLinkedList(LinkedList):
    def __init__(self, values: list[BiDirectionalNode]):
        head = values[0]
        curr = head
        for i in range(1, len(values)):
            curr.next = values[i]
            curr.next.prev = curr
            curr = curr.next
        super().__init__(head)
        self.tail = values[-1]

    def traverse_and_print(self):
        curr = self.head
        print("Traverse forward")
        while curr:
            print(curr.value, end="->")
            curr = curr.next
        print()

    def traverse_back_and_print(self):
        curr = self.tail
        print("Traverse backward")
        while curr:
            print(curr.value, end="->")
            curr = curr.prev
        print()

    def delete_specific_node(self, node):
        print("Deleting node: ", node.value)
        if self.head == node and self.tail == node:
            self.head = self.tail = None
            return

        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
            return

        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        curr = self.head
        while curr.next is not None and curr.next != node:
            curr = curr.next

        if curr.next == node:
            curr.next = curr.next.next
            curr.next.prev = curr


if __name__ == '__main__':
    n1 = BiDirectionalNode(2)
    n2 = BiDirectionalNode(5)
    n3 = BiDirectionalNode(7)
    n4 = BiDirectionalNode(10)
    n5 = BiDirectionalNode(12)

    linked_list = DoublyLinkedList([n1, n2, n3, n4, n5])
    linked_list.traverse_and_print()
    linked_list.traverse_back_and_print()

    linked_list.delete_specific_node(n3)
    linked_list.traverse_and_print()
    linked_list.traverse_back_and_print()

    linked_list.delete_specific_node(n5)
    linked_list.traverse_and_print()
    linked_list.traverse_back_and_print()

    linked_list.delete_specific_node(n1)
    linked_list.traverse_and_print()
    linked_list.traverse_back_and_print()

    linked_list.delete_specific_node(n2)
    linked_list.delete_specific_node(n4)
    linked_list.traverse_and_print()
    linked_list.traverse_back_and_print()