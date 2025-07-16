# You are provided with two lists of integers, listA and listB.
# Your task is to determine if listB is a contiguous sublist of listA. 
# You need to return True if listB is a contiguous sublist of listA, and False otherwise.
# A sublist is defined as a subset of consecutive elements within a list. 
# For instance, [2, 3] is a sublist of [1, 2, 3, 4] but not a sublist of [1, 3, 2, 4].
# Note that you are not allowed to use any built-in Python functions for this task except for the len() function to get the length of a list. 
# All other operations should be executed with basic Python programming constructs


# How i wrote it: 
def solution(listA, listB):
    length_a = len(listA)
    length_b = len(listB)
    
    for i in range(length_a):
    # Make sure we can find another sub list in what's currently left of the main list.  
        if i + length_b <= length_a:
          if  listA[i : i + length_b] == listB:
              return True
    return False          
print(solution([5, 4, 3, 2, 1], [3, 2, 1]))

# How GPT wrote it:
def is_contiguous_sublist(listA, listB):
    length_a = len(listA)
    length_b = len(listB)
    
    # If listB is longer than listA, it cannot be a sublist
    if length_b > length_a:
        return False

    # Loop through listA, stopping when there aren’t enough elements left for a match
    for i in range(length_a - length_b + 1):
        # Check if the sublist starting at index i matches listB
        match = True
        for j in range(length_b):
            if listA[i + j] != listB[j]:
                match = False
                break
        if match:
            return True

    return False

# Test cases
print(is_contiguous_sublist([5, 4, 3, 2, 1], [3, 2, 1]))  # Output: True
print(is_contiguous_sublist([5, 4, 3, 2, 1], [2, 1, 4]))  # Output: False
