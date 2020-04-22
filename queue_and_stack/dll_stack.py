import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # head and tail will make it easy to implement first in last out 
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        try:
            return self.storage.remove_from_tail()
        except:
            return None

    def len(self):
        return self.storage.__len__()
