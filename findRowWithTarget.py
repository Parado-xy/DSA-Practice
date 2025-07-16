# You are given a matrix of integers where every row and column are sorted in ascending order. 
# Your task is to find the row that contains a specific target value.
# It is guaranteed that target exists in the given matrix.
# The expected time complexity is O(n+m), where n is the number of rows and m is the number of columns.


# My answer:
def find_row_with_target(matrix: list[list[int]], target: int) -> int | None:
    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return row
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    
    return None
  
# Here's a breakdown of everything as given by ChatGPT:
# Here is the full question and code with detailed comments for clarity:

# ---

# **Question:**

# You are given a matrix of integers where every row and column is sorted in ascending order.  
# Your task is to find the row that contains a specific target value.  
# It is guaranteed that the target exists in the given matrix.  
# The expected time complexity is \(O(n + m)\), where \(n\) is the number of rows and \(m\) is the number of columns.

# ---

# ```python
# def find_row_with_target(matrix: list[list[int]], target: int) -> int | None:
#     # Start at the top-right corner of the matrix
#     row, col = 0, len(matrix[0]) - 1  # `row` points to the first row, `col` starts at the last column
    
#     # Continue searching until we either find the target or exhaust matrix bounds
#     while row < len(matrix) and col >= 0:
#         # Check if the current element is the target
#         if matrix[row][col] == target:
#             return row  # If found, return the current row index
        
#         # If the current element is less than the target, move down to the next row
#         elif matrix[row][col] < target:
#             row += 1
        
#         # If the current element is greater than the target, move left to the previous column
#         else:
#             col -= 1
    
#     # If the loop completes without finding the target, return None
#     return None
# ```

# ---

# **Explanation of the Code:**

# 1. **Initialize the Search Position**:
#    - We begin at the top-right corner of the matrix (`matrix[0][last_column]`), allowing us to use both row and column movements effectively.

# 2. **While Loop**:
#    - This loop continues as long as the row and column indices are within matrix bounds.
   
# 3. **Comparison Logic**:
#    - If the current element matches the `target`, we return the row index.
#    - If the current element is less than `target`, it means all elements to the left in the current row are also less, so we move **down** to the next row.
#    - If the current element is greater than `target`, it means all elements below in the current column are also greater, so we move **left** to the previous column.
   
# 4. **End of Search**:
#    - If the loop exits without finding the target (although the problem guarantees the target’s presence), the function would return `None` as a safeguard.

# **Time Complexity**:  
# The solution is \(O(n + m)\) because we move either one row down or one column left in each iteration, which is optimal for a matrix with sorted rows and columns.