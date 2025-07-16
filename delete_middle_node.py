#!/usr/bin/python


import random

# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

#    Method to append new nodes to the list
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

#    Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



def delete_middle(linked_list: LinkedList)-> None:
    """
    Deletes the middle node of a singly linked list, given only access to that node.
    """

    # Create Pointers;
    slow = linked_list.head
    fast = linked_list.head
    prev = None

    # Loop through;
    # Note that the fast pointer moves twice as fast as the slow pointer;
    # And the coditional check should be fast and fast.next so we don't stop the loop premsturely for odd and even elements;
    # This ensures that the middle node falls at [n//2] for even elements and [n//2] + 1 for odd elements;
    while (fast and fast.next): # While the faster pointer has somewhere to go, keep looping;
        # update the previous pointer;
        prev = slow
        # update the slow pointer;
        slow = slow.next
        # update the fast pointer;
        fast = fast.next.next




    # if prev, remove the current node from the linked list;
    if prev:
        prev.next = slow.next
        slow.next = None
    else:
        # if no previous node, it means we've only got between one and two elements;
        if (linked_list.head == slow):
            prev = slow
            linked_list.head.next = None
            prev.next = None
            return linked_list.head
        

    return linked_list.head

def generate_random_linked_list(size, lower_bound=1, upper_bound=10):
    linked_list = LinkedList()
    for _ in range(size):
        linked_list.append(random.randint(lower_bound, upper_bound))
    return linked_list

# Generate a random linked list with 10 nodes, values between 1 and 10
random_linked_list = generate_random_linked_list(5)

random_linked_list.print_list() # Print the linkedlist

delete_middle(random_linked_list) # remove middle element of the linked list;

random_linked_list.print_list() # Print the linkedlist


        


    
# DeepSeeks Code: 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         if not self.head:
#             self.head = Node(data)
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = Node(data)

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# def delete_middle(linked_list: LinkedList) -> None:
#     if not linked_list.head:
#         return None

#     # Edge case: single node
#     if not linked_list.head.next:
#         linked_list.head = None
#         return None

#     slow = linked_list.head
#     fast = linked_list.head
#     prev = None

#     # Use fast and slow pointers to find the middle
#     while fast and fast.next:
#         prev = slow
#         slow = slow.next
#         fast = fast.next.next

#     # Delete the middle node (slow)
#     if prev:
#         prev.next = slow.next
#     else:
#         # Only two nodes, delete the second node (slow)
#         linked_list.head.next = None

#     return linked_list.head

# # Example usage:
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# print("Original list:")
# ll.print_list()
# delete_middle(ll)
# print("After deleting middle node:")
# ll.print_list()