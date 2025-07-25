# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106


class Solution:
    # This solution ic correct, but caused a TLE. 
    def countPrimes(self, n: int) -> int:

        # We'll use the concept of the sieve of Eratosthenes
        
        # Let's have a variable called thresh. If below that tresh, you have zero primes.
        tresh = 2
        if (n < tresh):
            return 0

        # Create a boolean array of numbers from [2-n); 
        values = [True for _ in range(2, n)] # We assume every value is a prime. 

        # Perform a Sieve. 
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if (values[j] == False):
                    continue

                # If the index of j is a multiple of i . 
                if (j + 2) % (i + 2) == 0:
                    values[j] = False # J is divisible by something other than itself and is therefore not a prime. 
        # Since a value of True is equivalent to 1, we can sum up the array to know the amount of primes.
        return sum(values)

    def countPrimes_COPILOT_OPTIMIZED(self, n: int) -> int:
            """
            Optimized Sieve of Eratosthenes
            Time: O(n log log n), Space: O(n)
            """
            if n < 2:
                return 0
            
            # Create boolean array for numbers [0, n)
            # Index i represents number i
            is_prime = [True] * n
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            
            # Sieve process
            for i in range(2, int(n**0.5) + 1):  # Only need to check up to sqrt(n)
                if is_prime[i]:  # If i is still marked as prime
                    # Mark all multiples of i as non-prime
                    # Start from i*i (smaller multiples already handled)
                    for j in range(i * i, n, i):
                        is_prime[j] = False
            
            # Count remaining primes
            return sum(is_prime)
    

# WIkipedia link to Related Article. 
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes