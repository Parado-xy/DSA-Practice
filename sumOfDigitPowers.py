# Question:
# You are provided with a positive integer n. Your task is to write a recursive function 
# that returns the sum of all the digits in n raised to the power of their respective positions 
# (1-indexed from the right). Make sure to use recursion in your solution.
#
# In simpler terms, take each digit in n, raise it to the power of its position, 
# and find the sum of these values. Note that positions start from 1 and count from the rightmost digit.
#
# For example, if n = 253, your function should calculate 3^1 = 3 (as 3 is at the 1st position), 
# 5^2 = 25 (as 5 is at the 2nd position), and 2^3 = 8 (as 2 is at the 3rd position), 
# with each ^ representing "raised to the power of". 
# So, the final result will be 3 + 25 + 8 = 36.

# Answer:
def sum_of_digit_powers(n, pos=1):
    # Base Case: Single digit left in n
    if n < 10:
        return n ** pos
    else:
        # Recursive Case: Process last digit and move to next
        last_digit = n % 10
        current_sum = last_digit ** pos
        return current_sum + sum_of_digit_powers(n // 10, pos + 1)

# Example usage:
print(sum_of_digit_powers(253))  # Output: 36
