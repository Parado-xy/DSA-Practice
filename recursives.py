# You are tasked with creating a function get_sum(n) that calculates the sum of all the numbers from n to 1 using recursion.
# For instance, get_sum(5) should result in 15 (5 + 4 + 3 + 2 + 1 = 15), while get_sum(1) should yield 1.

def get_sum(n):
    # Base Case
    if n <= 1:
        return 1
    # Recursive Case    
    else:
        return n + get_sum(n - 1)    
    

# The task is to write a recursive function recursive_countdown(n) that takes an integer n as an input and returns a list of integers from n to 1, inclusive, in decreasing order.
# Make sure to use recursion in this task.
# For example, for n = 5, the output should be [5, 4, 3, 2, 1].
#
def recursive_countdown(n):
    # Base Case:
    if n <= 1:
        return [n]
    # Recursive Case    
    else:
        return [n] + recursive_countdown(n - 1)    
        