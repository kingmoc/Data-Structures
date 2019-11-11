import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        DoublyLinkedList().add_to_head(value)

    def dequeue(self):
        pass

    def len(self):
        return self.size

