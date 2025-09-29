import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Input validation. 
        if not grid: 
            return 0

        # Row& Column count. 
        rows, cols = len(grid), len(grid[0])
        # We can place hashable tuples of (r, c) in the set.
        visited = set()
        # Island count; 
        islands = 0

        # Breadth first search algo.
        def bfs(r, c):
            # A queue data structure. 
            queue = collections.deque()
            # Set the current island to visited. 
            visited.add((r, c))
            # Add this island to the queue. 
            queue.append((r, c))

            # The directions we need to check for connected islands. 
            directions = [
                [1, 0], # Down 
                [-1, 0], # Up
                [0, 1], # Left
                [0, -1] # Right. 
            ]

            # While there are nodes to be processed in the queue. 
            while queue:
                # Remove from the frontier. 
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # If the current row is in the range of rows,
                    # and if the current column is in the range of columns. 
                    # if the current spot is an island,
                    # and that island hasn't been visited,
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visited):
                        # Expand Frontier
                        queue.append((r, c))
                        # Mark expanded frontier as visited. 
                        visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                # If the current index is an island, and we've not been here
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Let's conduct breadth-first search on the island. 
                    bfs(r, c)
                    # mark the siland as visited. 
                    visited.add((r, c))
                    # Increment the count of islands. 
                    islands += 1

        return islands

    

