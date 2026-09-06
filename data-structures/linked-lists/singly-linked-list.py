from node import Node
from base import LinkedList

class SinglyLinkedList(LinkedList):
    def __init__(self, values:list[Node]):
        head = values[0]
        curr = head
        for i in range(1, len(values)):
            curr.next = values[i]
            curr = curr.next
        super().__init__(head)

    def traverse_and_print(self):
        print("Traverse forward")
        curr = self.head
        while curr:
            print(curr.value, end="->")
            curr = curr.next
        print()

    def delete_specific_node(self, node:Node):
        print("Deleting node: ", node.value)
        if self.head == node:
            self.head =  self.head.next
            return

        curr = self.head
        while curr.next is not None and curr.next != node:
            curr = curr.next

        if curr.next == node:
            curr.next = curr.next.next

        return

if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(10)
    n3 = Node(2)
    n4 = Node(7)

    linked_list = SinglyLinkedList([n3, n1, n4, n2])
    linked_list.traverse_and_print()

    linked_list.delete_specific_node(n2)
    linked_list.traverse_and_print()

    linked_list.delete_specific_node(n1)
    linked_list.traverse_and_print()

    linked_list.delete_specific_node(n3)
    linked_list.delete_specific_node(n4)
    linked_list.traverse_and_print()