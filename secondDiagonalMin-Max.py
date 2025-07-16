# Given a square matrix grid of integers, your task is to find the minimum and maximum values at the secondary diagonal. 
# The secondary diagonal starts at the top right corner and ends at the bottom left corner.
# Return a list of two elements where the first element is the minimum value, and the second is the maximum value that you have found in the diagonal. 
# If the square matrix is empty, return [None, None].
# The time complexity of the solution should not exceed O(n), where n is the length of the row (or column) in the grid.

# My Solution
def min_max(grid):
    arr = []
    count = 0
    for i in range(len(grid) - 1, -1, -1):
        arr.append(grid[count][i])
        count += 1         
    
    if len(arr) != 0:    
         return [min(arr), max(arr)]
    else:
        return  [None, None]
print(min_max([[1,2,3],[4,5,6],[7,8,9]]))        

# GPT's thoughts on further optimization:
# Your solution works well to identify the elements in the secondary diagonal and then find the minimum and maximum values. However, there is a way to improve it by keeping track of the minimum and maximum values directly while iterating, instead of creating an intermediate list `arr`. This keeps the complexity strictly at \(O(n)\) in both time and space.

# Here’s an optimized version without the extra list:

# ```python
# def min_max(grid):
#     if not grid:
#         return [None, None]
    
#     n = len(grid)
#     min_val = max_val = grid[0][n - 1]  # Start from the top-right corner (first element of the secondary diagonal)
    
#     for i in range(1, n):
#         diag_val = grid[i][n - i - 1]
#         min_val = min(min_val, diag_val)
#         max_val = max(max_val, diag_val)
        
#     return [min_val, max_val]
# ```

# ### Explanation
# 1. **Initialization**: Set `min_val` and `max_val` to the first element on the secondary diagonal, `grid[0][n - 1]`.
# 2. **Single Loop**: Use one loop to iterate down the secondary diagonal. The position of each element in the diagonal is `grid[i][n - i - 1]`.
# 3. **Update**: Update `min_val` and `max_val` in each iteration.
# 4. **Return**: Return `[min_val, max_val]` after the loop ends.

# ### Complexity
# - **Time Complexity**: \(O(n)\), as we only need one loop through the secondary diagonal.
# - **Space Complexity**: \(O(1)\), as we do not create additional lists.        