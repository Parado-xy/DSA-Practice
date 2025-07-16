# Problem Description:
# Given an integer num, determine if it is a palindrome.
# A palindrome reads the same forwards and backwards. Negative numbers are not palindromic.
# Additionally, do this without converting the integer to a string.

# Example 1:
# Input: num = 121
# Output: True (since 121 reads the same forwards and backwards)

# Example 2:
# Input: num = -121
# Output: False (negative numbers cannot be palindromic)

# Constraints:
# -2^31 <= num <= 2^31 - 1

# Difficulty Level: Medium (follow-up constraint)
# Explanation:
# Without the ability to convert the integer into a string, this question moves up in difficulty.
# Instead, the solution involves reversing the integer by processing individual digits
# and reassembling them in reverse order. This requires manual handling of digit extraction,
# integer manipulation, and edge case considerations.

def is_palindrome(num: int) -> bool:
    # Edge case: negative numbers are not palindromic
    if num < 0:
        return False
    
    # Save the original number to compare later
    saved = num
    reversed_num = 0
    
    # Reverse the integer by processing each digit
    while num > 0:
        # Extract the last digit
        last_digit = num % 10
        # Append the last digit to the reversed number
        reversed_num = reversed_num * 10 + last_digit
        # Remove the last digit from num
        num //= 10
    
    # Check if the reversed number matches the original number
    return saved == reversed_num

print(is_palindrome(1_000_890)) # False
print(is_palindrome(123456789987654321)) # True