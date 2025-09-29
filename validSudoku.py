# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

class Solution:
    def valid_sudoku(self, board):
        ...

    def valid_row(self, row_index, board):
        rows = set()

        # Elements
        for element in board[row_index]:
            # Skip the dot placeholders.
            if element == '.':
                continue
            # if the element has not been seen before, add it to the set
            if element not in rows:
                rows.add(element)
            else:
                # We return false if the element is in the rows
                return False
        # if we get to this point, return true
        return True
        
    def valid_column(self, column_index, board):
        # A set for the column. 
        column = set()
        
        for row in board:
            if row[column_index] != '.':
                continue 
            if row[column_index] not in column:
                column.add(row[column_index])
            else:
                return False
            
        return True
    
    def valid_3_x_3_grid(self, board):
        start_row, start_column = 0, 0

        