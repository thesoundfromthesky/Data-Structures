"""
### Doubly Linked Lists
 * The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
 * The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.
   * `add_to_head` replaces the head of the list with a new value that is passed in.
   * `add_to_tail` replaces the tail of the list with a new value that is passed in.
   * `remove_from_head` removes the head node and returns the value stored in it.
   * `remove_from_tail` removes the tail node and returns the value stored in it.
   * `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 
   * `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 
   * `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
   * `get_max` returns the maximum value in the list. 
 * The `head` property is a reference to the first node and the `tail` property is a reference to the last node.
 
![Image of Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)
"""


"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

nodes = ListNode(0)
nodes.insert_after(1)
nodes.next.insert_after(2)
nodes.next.next.insert_after(3)
nodes.next.next.next.insert_after(4)

def reverse_list(head):
    n_prev = None
    n_cur = head
    n_next = None
    while n_cur:
        n_next = n_cur.next
        n_cur.next = n_prev
        n_prev = n_cur
        n_cur = n_next
    return n_prev


node_cur = reverse_list(nodes)
node_val = node_cur.value
while True:
    print(node_val)
    node_cur = node_cur.next
    if node_cur is None:
        break
    node_val = node_cur.value

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
          value = self.head.value
          self.delete(self.head)
          return value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
          value = self.tail.value
          self.delete(self.tail)
          return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
          if node is self.head:
              return
          self.add_to_head(node.value)
          self.delete(node)
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
          if node is self.tail:
              return
          self.add_to_tail(node.value)
          self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1

        if self.head is self.tail:
            self.head = None
            self.tail = None
        
        elif node is self.head:
            self.head = node.next
            node.delete()
        
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        max = self.head.value
        
        while(current is not None):
            if current.value > max:
                 max = current.value
            current = current.next
        return max
