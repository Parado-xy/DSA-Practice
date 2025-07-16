import functools

# The best way to make the memoized function was to first write a staandard factorial function and move from
# there. 

# Standard recursive factorial (no memoization)
def factorial_standard(n):
    if n <= 1:
        return 1
    return n * factorial_standard(n - 1)

# Memoized factorial using dictionary
def factorial_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return 1
    
    memo[n] = n * factorial_memo(n - 1, memo)
    return memo[n]

# Memoized factorial using functools decorator
@functools.lru_cache(maxsize=None)
def factorial_lru_cache(n):
    if n <= 1:
        return 1
    return n * factorial_lru_cache(n - 1)





# Memoization is an optimization technique primarily used in dynamic programming to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

# Key Characteristics of Memoization:
# - It's a form of caching
# - Stores results of expensive function calls
# - Trades memory space for computational speed
# - Most effective for functions with:
#   - Repetitive calculations
#   - Deterministic outputs (same input always produces same output)

# How Memoization Works:
# 1. First time a function is called with specific inputs, compute the result
# 2. Store the result in a cache (usually a dictionary or hash table)
# 3. On subsequent calls with same inputs, return cached result instead of recomputing

# Common Use Cases:
# - Recursive algorithms
# - Fibonacci sequence calculation
# - Factorial computations
# - Dynamic programming problems
# - Recursive mathematical functions

# Example Patterns:
# 1. Manual Memoization (using a dictionary)
# ```python
# def fibonacci_memo(n, memo=None):
#     if memo is None:
#         memo = {}
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
#     return memo[n]
# ```

# 2. Python's `functools.lru_cache` Decorator
# ```python
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# ```

# Pros of Memoization:
# - Dramatically reduces time complexity
# - Prevents redundant calculations
# - Can transform exponential time algorithms to linear time
# - Easy to implement

# Cons of Memoization:
# - Increases memory usage
# - Overhead for simple or non-recursive functions
# - Not useful for functions with unique inputs each time

