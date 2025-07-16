# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0. 
# [['','','',''],
#  ['','','',''],
#  ['','','','']]


import random
import pprint

def generate_matrix(m, n, zero_prob=0.2):
    """Generate an MxN matrix with random integers and some zeros.
    
    Args:
        m: Number of rows.
        n: Number of columns.
        zero_prob: Probability of a zero being placed in a cell.
        
    Returns:
        A randomly generated MxN matrix.
    """
    matrix = []
    for _ in range(m):
        row = []
        for _ in range(n):
            if random.random() < zero_prob:
                row.append(0)
            else:
                row.append(random.randint(1, 9))
        matrix.append(row)
    return matrix

# Example usage:
m, n = 5, 6  # Change m, n as per your needs
matrix = generate_matrix(m, n)


def infect(matrix : list[list]) -> list[list]: 
    infected_rows = set()
    infected_columns = set()
    for row, _ in enumerate(matrix):
        for column, column_value in enumerate(matrix[row]):
            if column_value == 0:
                infected_rows.add(row)
                infected_columns.add(column)

    def row_to_zeros():
        for i in infected_rows:
            matrix[i] = [0 for num in range(len(matrix[0]))]

    def column_to_zero():
        for i in matrix:
            # Sets all the infected columns to zero
            for j in infected_columns:
                i[j] = 0       

    row_to_zeros()
    column_to_zero()             

    return  matrix   
    
pprint.pprint(matrix)
pprint.pprint(infect(matrix))                