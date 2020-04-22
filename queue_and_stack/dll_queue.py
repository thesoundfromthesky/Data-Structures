import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # We can reuse functions implemented in DLL.
        # first in first out
        self.storage = DoublyLinkedList()
 
    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        try:
            return self.storage.remove_from_head()
        except:
            return None

    def len(self):
        return self.storage.__len__()
