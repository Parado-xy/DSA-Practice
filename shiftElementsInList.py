#In this problem, you are given a list of n integers. 
# Additionally, you are given an integer shift, 
# which represents the number of positions each element in the list should be moved. 
# Your task is to create a Python function that should shift every element in the list to the right (for a positive shift) or to the left (for a negative shift) by shift positions.
# The shift should be circular — the last element should be moved to the start of the list if shift is positive, and vice versa.
# Please implement this without the usage of any built-in functions of Python to shift, sort, or move items in the list.
# Your solution’s efficiency should be O(n). 


def shift_list_elements(ls, shift):
    # Adjust shift to be within the bounds of the list length
    n = len(ls)
    shift = shift % n  # Ensures shift is within the range [0, n)
    
    # Create an empty list of the same length to store shifted elements
    result = [0] * n
    
    # Perform the circular shift
    for i, value in enumerate(ls):
        result[(i + shift) % n] = value
        
    return result

# Test cases
print(shift_list_elements([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(shift_list_elements([1, 2, 3, 4, 5], -2)) # Output: [3, 4, 5, 1, 2]


# Shift list elements:
def shift_list_elements_simplified(ls, shift):
    # TODO: Implement the solution
    # The Shift is periodic around the length of the array. 
    # Create an empty list of the same length to store shifted elements
    zeroes = [0 for _ in range(len(ls))]
    
    for i,value in enumerate(ls):
        # Perform the circular shift
        zeroes[(i + shift) % len(ls)] = value
    return zeroes

print(shift_list_elements_simplified([1, 2, 3, 4, 5], 2))