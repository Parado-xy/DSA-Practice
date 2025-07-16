#!/bin/python3
def dfs(graph, start, visited=None):
    # Define the dfs function which takes three parameters:
    # graph: the graph represented as an adjacency list
    # start: the starting node for the DFS traversal
    # visited: a set to keep track of visited nodes (default is None)

    if visited is None:
        # If visited is not provided, initialize it as an empty set
        visited = set()

    # Add the starting node to the set of visited nodes
    visited.add(start)
    # Print the current node (start) followed by a space, without a newline
    print(start, end=" ")

    # Iterate over all the neighbors of the current node (start)
    for neighbor in graph[start]:
        # If the neighbor has not been visited yet
        if neighbor not in visited:
            # Recursively call dfs on the neighbor
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['F', 'D'],
    'C': [],
    'D': ['G', 'I'],
    'E': ['H'],
    'F': ['E'],
    'G': [],
    'H': ['G'],
    'I': []
}

dfs(graph, 'A')