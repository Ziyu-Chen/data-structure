class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


# Don't forget to update the head, tail and length of the linked list!!!
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        # It checks whether the linked list is empty. 
        # It returns True if it is empty and False if it is not.

        return

    def get_tail(self):
        # It finds the current tail of the linked list and returns it.
        # It is used to update self.tail when self.tail is no longer pointing to the last node of the linked list, but it doesn't directly update the self.tail here.

        return
        
    def to_list(self):
        # It converts the linked list to a regular list.
        # It returns a list that contains all the node values in the linked list.

        return

    def index(self, value):
        # It returns the position of the first node that has the same value as the given value. (Assuming that the head is at position 0, the second node is at position 1...)
        # It returns -1 if the value is not in the linked list.

        return
    
    def at_index(self, position):
        # It returns the value of the node at the given position. (Assuming that the head is at position 0, the second node is at position 1...)
        # It raises an exception if the position doesn't exist in the linked list.

        return

    def append(self, value):
        # It generates a new node with the given value and adds it behind the tail of the linked list.

        return

    def left_append(self, value):
        # It generates a new node with the given value and adds it in front of the head of the linked list. 

        return

    def insert(self, position, value):
        # It generates a new node with the given value and inserts it at the given position. (Assuming that the head is at position 0, the second node is at position 1...)
        # It raises an exception if insertion at the given position is impossible.

        return
    
    def remove(self, position):
        # It removes the node at the given position. (Assuming that the head is at position 0, the second node is at position 1...)
        # It returns the value of the removed node.
        # It raises an exception if the given position doesn't exist in the linked list or the linked list is empty.

        return
    
    def pop(self):
        # It removes the last node in the linked list.
        # It returns the value of the removed node.

        return
    
    def left_pop(self):
        # It removes the first node in the linked list.
        # It returns the value of the removed node.

        return

    def remove_first(self, value):
        # It removes the first node whose value is equal to the given value in the linked list.
        # It returns the position of the removed node. (Assuming that the head is at position 0, the second node is at position 1...)
        # It raises an exception if the given value doesn't exist in the linked list or the linked list is empty.

        return

    def find_min(self):
        # It returns the minimum value in linked list.
        # It ruturns None if the linked list is empty.

        return
    
    def find_max(self):
        # It returns the maximum value in linked list.
        # It ruturns None if the linked list is empty.

        return
    
    def count(self, value):
        # It returns the number of occurrences of the given value in the linked list.

        return
    
    def reverse(self):
        # It reverses the linked list.

        return
