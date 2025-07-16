def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number recursively.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. 

    This recursive implementation breaks down the problem into smaller subproblems, 
    calculating F(n) as F(n-1) + F(n-2). 

    However, this approach is inefficient for larger values of n due to redundant calculations.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """

    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """
    Calculates the nth Fibonacci number iteratively.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

    This iterative approach is more efficient than the recursive one, as it avoids redundant calculations.
    It calculates each Fibonacci number sequentially, storing the previous two values.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """

    if n <= 1:
        return n

    fib_prev, fib_next = 0, 1
    for _ in range(2, n + 1):
        fib_prev, fib_next = fib_next, fib_prev + fib_next
    return fib_next

# Example usage:
n = 10
print("Recursive Fibonacci:", fibonacci_recursive(n))
print("Iterative Fibonacci:", fibonacci_iterative(n))





from typing import List

# The provided Python function `is_toeplitz_matrix` efficiently determines whether a given 2D matrix is a Toeplitz matrix.

# **Toeplitz Matrix Recap:**

# A Toeplitz matrix is a special type of matrix where each descending diagonal from left to right is constant. 
# This means that elements on a diagonal parallel to the main diagonal are identical.

# **Function Breakdown:**

# 1. **Input:**
#    - The function takes a 2D list `matrix` as input, representing the matrix to be checked.

# 2. **Initialization:**
#    - `rows` and `cols` store the number of rows and columns in the matrix, respectively.

# 3. **Iterative Checking:**
#    - The function iterates through the matrix, starting from the second row and the second column (indices 1, 1).
#    - For each element at position `(i, j)`, it compares it with the element diagonally above and to the left, which is at position `(i-1, j-1)`.
#    - If any pair of compared elements is different, the matrix is not Toeplitz, and the function immediately returns `False`.

# 4. **Returning the Result:**
#    - If the loop completes without finding any mismatched elements, it means the matrix is Toeplitz, and the function returns `True`.

# **Why This Approach Works:**

# - **Diagonal Comparison:** By comparing elements on diagonals, the function ensures that each diagonal has a constant value.
# - **Early Termination:** If a mismatch is found, the function immediately returns `False`, avoiding unnecessary iterations.
# - **Efficient Iteration:** The function iterates through the matrix efficiently, starting from the second row and column, as the first row and column don't contribute to diagonal comparisons.

# **Example:**

# Consider the following Toeplitz matrix:

# ```
# 1 2 3 4
# 5 1 2 3
# 6 5 1 2
# 7 6 5 1
# ```

# The function would compare:
# - `matrix[1][1]` with `matrix[0][0]`
# - `matrix[1][2]` with `matrix[0][1]`
# - ... and so on

# If all comparisons are true, the function concludes that the matrix is Toeplitz.

# By systematically checking the diagonals, this function provides an accurate and efficient way to determine the Toeplitz property of a given matrix.


def is_toeplitz(matrix: List[List[int]]) -> bool:
  """
  Checks if a given matrix is a Toeplitz matrix.

  Args:
    matrix: A 2D list representing the matrix.

  Returns:
    True if the matrix is Toeplitz, False otherwise.
  """

  rows, cols = len(matrix), len(matrix[0])
  for i in range(1, rows):
    for j in range(1, cols):
      if matrix[i][j] != matrix[i - 1][j - 1]:
        return False
  return True

# Example usage:
matrix = [[1, 2, 3, 4],
          [5, 1, 2, 3],
          [6, 5, 1, 2],
          [7, 6, 5, 1]]

print(is_toeplitz(matrix))  # Output: True         
      
                