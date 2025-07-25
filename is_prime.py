# We can identify if a number is prime by iterating from 2 to the squareroot of the number, if the number is devisible 
# By any of those, it's not a prime number, else it is. 
# Note that negative numbers aren't prime numbers because they don't fit the definition of prime numbers. 
# **A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.**

# In simpler terms, a prime number is a number that can only be divided evenly by 1 and itself. 

# For example:
# * 2 is a prime number because it can only be divided by 1 and 2.
# * 5 is a prime number because it can only be divided by 1 and 5.
# * 9 is *not* a prime number because it can be divided by 1, 3, and 9. 

# So, prime numbers are essentially the building blocks of numbers. 

import math
def is_prime(n):
    """Function to check if n is a prime number"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(10)) # Outputs: False
print(is_prime(11)) # Outputs: True

import math

def is_perfect_square(num):
    """
    Determines if a given number is a perfect square.

    A perfect square is an integer that can be expressed as the square of another integer.

    Args:
        num: The number to check.

    Returns:
        True if `num` is a perfect square, False otherwise.
    """

    root = int(math.sqrt(num))  # Calculate the integer square root
    return root * root == num  # Check if the square of the root equals the original number

import math

def is_prime_gpt(n):
    """
    Determines if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    Args:
        n: The number to check for primality.
    Returns:
        True if n is prime, False otherwise.
    """

    # Handle base cases: numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Iterate from 2 to the square root of n to check for divisors
    for i in range(2, int(math.sqrt(n)) + 1):
        # If n is divisible by i, it's not prime
        if n % i == 0:
            return False

    # If no divisors are found, n is prime
    return True



def get_prime_factors(n):
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True        
        
    def contains_factors(arr, n):
        for i in arr:
            if n % i == 0:
                return True
        return False    

    factors = []
    
    if is_prime(n):
        factors.append(n)
        return factors
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if contains_factors(factors, i):
                continue
            else:
                factors.append(i)
                
    for i in factors:
        while n % i == 0:
            n /= i
    # Any value remaining that's greater than 1 is a prime factor greater than the sqrt(n)        
    if n != 1.0:        
        factors.append(int(n))                    
                       
            
    return factors        
print(get_prime_factors(97))