#!/usr/bin/python

# The goal here is to reverse a Linked List.
# We can achieve this by traversing the linked list, then setting the next pointer of each node to the prev node.
# Then we can just return the last node which is now the head of the reversed node. 

import random

# Node class to represent each element in the linked list
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

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


def reverse_linked_list(linked_list: LinkedList):
    """
    The Goal here is to reverse a linked-list without any additional data structure. 
    """

    # initiate variables, current and prev. 
    current = linked_list.head
    prev = None

    # while we have somewhere to go i.e we haven't reached the end of the linkedlist
    while current:
        # Save the actual next node.
        next_node = current.next
        # Point the current node's pointer backward
        current.next = prev
        # make the previous pointer point at the current node.
        prev = current
        # set the current node to the next node which could be "None" or Node
        current = next_node

    # Return prev which will point at the last node. 
    return prev    

# Function to manually traverse the linked list and print each node's value
def manual_traverse(linked_list):
    
    current = linked_list
    while current:
        print(f"{current.data} ->", end=' ')
        current = current.next
    print("None")


def generate_random_linked_list(size, lower_bound=1, upper_bound=10):
    linked_list = LinkedList()
    for _ in range(size):
        linked_list.append(random.randint(lower_bound, upper_bound))
    return linked_list

# Generate a random linked list with 10 nodes, values between 1 and 10
random_linked_list = generate_random_linked_list(5)

random_linked_list.print_list() # Print the linkedlist

manual_traverse(reverse_linked_list(random_linked_list)) # move through the reversed linked-list and print out each node.
