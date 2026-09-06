from abc import ABC, abstractmethod
from node import Node

class LinkedList(ABC):
    def __init__(self, head:Node):
        self.head = head

    @abstractmethod
    def traverse_and_print(self):
        pass

    @abstractmethod
    def delete_specific_node(self, node:Node):
        pass