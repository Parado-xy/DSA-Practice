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


def kth_to_last(linked_list: LinkedList, k: int) -> Node:
    """
    Removes and returns the Kth-to-last element from a singly linked list.
    """

    # Start The Runner and the current node at the head
    current = linked_list.head
    runner = current
    # Initiate previous node to None
    prev = None

    # adjust k for runner use;
    k -= 1

    # Move runner k - 1 steps ahead of current; 
    while (k > 0) and (runner.next != None):
        runner = runner.next
        k -= 1

    # Now traverse both pointers till the runner reaches the end of the linked list
    while runner.next:
        # update the previous pointer;
        prev = current        
        # update the regular pointer;
        current = current.next
        # update the runner that's k - 1 units ahead
        runner = runner.next  


    # if prev, remove the current node from the linked list;
    if prev:
        prev.next = current.next
    else:
        # if no previous node, it means we've only got between one and three elements;
        # In that case, we return None || current.next because we have to remove that element from the linked list;
        if (linked_list.head == current) and (current != runner):
            return current.next
        else:
            return None     

    # set the current node's next to None
    current.next = None          

    return linked_list.head     
    

def generate_random_linked_list(size, lower_bound=1, upper_bound=10):
    linked_list = LinkedList()
    for _ in range(size):
        linked_list.append(random.randint(lower_bound, upper_bound))
    return linked_list

# Generate a random linked list with 10 nodes, values between 1 and 10
random_linked_list = generate_random_linked_list(10)

random_linked_list.print_list() # Print the linkedlist

kth_to_last(random_linked_list, 3) # remove third to the last element of the linked list;

random_linked_list.print_list() # Print the linkedlist

