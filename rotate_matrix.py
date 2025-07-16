#!/usr/bin/python3

from typing import List
import pprint

Matrix = List[List]

def rotate_matrix(matrix: Matrix ) -> Matrix:
    """
    Rotate a matrix 90 degrees, in-place;
    """
    # Rotating a Matrix Can be Done in 2 steps, Transposing, and then reversing; 
    # Let's Transpose; 
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # Swap rows and columns; 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # row,       # column        # column,     # row
    # Now let's reverse each row; 
    for arr in matrix:
        arr.reverse()

    

sample: Matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]            

rotate_matrix(sample)

pprint.pprint(sample)