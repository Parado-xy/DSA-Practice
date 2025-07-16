def get_prime_factors(n):
    """
    This function returns a list of all unique prime factors of an integer n.
    Prime factors are prime numbers that divide n without a remainder.
    The result is sorted in ascending order.
    
    Parameters:
        n (int): The integer to find prime factors of.
    
    Returns:
        List[int]: A list of unique prime factors in ascending order.
    """
    # Initialize an empty list to store unique prime factors.
    factors = []

    # Step 1: Remove all factors of 2 from n
    # ---------------------------------------------------
    # This initial loop handles the only even prime, 2.
    # We divide n by 2 repeatedly to ensure no even factors remain.
    while n % 2 == 0:
        if 2 not in factors:  # Check if 2 is already in the list to avoid duplicates.
            factors.append(2)
        n //= 2  # Divide n by 2 to remove the factor completely.

    # Step 2: Check for odd prime factors from 3 upwards
    # ---------------------------------------------------
    # Starting from 3, we check each odd number up to sqrt(n).
    # After removing all factors of 2, we skip even numbers.
    # This reduces the steps by focusing on odd divisors only.
    for i in range(3, int(n**0.5) + 1, 2):
        # As long as n is divisible by i, add i to the factors list.
        # Divide n by i until it no longer divides evenly.
        while n % i == 0:
            if i not in factors:  # Avoid duplicates by checking if i is already in the list.
                factors.append(i)
            n //= i  # Reduce n by dividing it by i.

    # Step 3: Handle the case where n is a prime greater than 2
    # ---------------------------------------------------
    # After dividing out all factors up to sqrt(n), if n > 2, 
    # it must be prime itself and should be included in the result.
    if n > 2:
        factors.append(n)

    return factors  # Return the list of unique prime factors.


# Example usage:
print(get_prime_factors(84))  # Output: [2, 3, 7]


