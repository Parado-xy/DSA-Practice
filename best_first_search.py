#!/bin/python3

# We're trying to Implement Best First Search Which uses a path function f

import heapq

def best_first_search(initial, goal, cost_func):
    priority_queue = []
    