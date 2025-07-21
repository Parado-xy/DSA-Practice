#!/bin/python3
# You're given a matrix where each row is sorted in ascending order. The columns are also sorted in ascending order.
# This creates a special pattern where the values in the matrix increase as you move right or down but decrease as you move left or up.
# Your task is to write a Python function that counts the number of integers in the matrix that are smaller than the given target. The function should return this count as an integer.
# The expected complexity is O(n + m), where n is the number of rows and  is the number of columns in the matrix.

from typing import List
# My first Try:
# This try only makes use of row-wise sorted order. 
# By trys to search only if necessary. 
def count_less_than(matrix: List[List], target):
    # TODO: Your code goes here. Remember that the matrix is sorted row-wise and column-wise!
    count = 0
    for i in range(len(matrix)):
        try:
            index = matrix[i].index(target)
            count += len(matrix[i][:index])
        except ValueError:
            if min(matrix[i]) < target:
                for i in matrix[i]:
                    if i < target:
                        count += 1
    return count

# My second approach 
# Based on this principle:
# Instead of iterating through each element, consider starting from the top-right corner of the matrix.
# Here's a hint:
# If the current element is less than the target, all elements in that row to the left are also less. 
# Move down to the next row. If the current element is greater than or equal to the target, move left to the previous column.
# This way, you can efficiently count the elements in O(n+m) time. 

def count_less_than_effective(matrix, target):
    row, count = 0, 0
    column = len(matrix[0]) - 1  # Start from the top-right corner

    while row < len(matrix) and column >= 0:
        if matrix[row][column] < target:
            # All elements in this row up to the current column are less than the target
            count += (column + 1)
            row += 1  # Move to the next row
        else:
            column -= 1  # Move left in the current row

    return count
               
# Test case
print(count_less_than_effective([[1, 2], [2, 3]], 2))  # Expected output: 1
