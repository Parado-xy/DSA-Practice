'''
Co-prime numbers, also known as relatively prime or mutually prime numbers, are pairs of numbers that have no common factor other than 1. This means their greatest common divisor (GCD) is 1.

**Examples of co-prime numbers:**

* (4, 7)
* (5, 9)
* (8, 15)
* (11, 13)

**Important Points:**

* **Co-prime numbers do not have to be prime numbers themselves.** For example, 4 and 9 are co-prime even though they are not prime numbers.
* **Two consecutive integers are always co-prime.** For example, (2, 3), (11, 12), and (99, 100) are co-prime pairs.
* **The sum of two co-prime numbers is always co-prime to their product.** For example, 2 + 3 = 5, and 2 * 3 = 6. Since 5 and 6 are co-prime, this property holds true.

**How to determine if two numbers are co-prime:**

1. **List the factors of each number:**
   * Factors of 4: 1, 2, 4
   * Factors of 7: 1, 7

2. **Identify common factors:**
   * The only common factor is 1.

3. **Conclude:**
   * Since the only common factor is 1, 4 and 7 are co-prime.

**Applications of co-prime numbers:**

* **Cryptography:** Co-prime numbers play a crucial role in various cryptographic algorithms, such as the RSA encryption algorithm.
* **Modular arithmetic:** Co-prime numbers are essential in modular arithmetic, which is used in various mathematical and computer science applications.
* **Number theory:** Co-prime numbers have many interesting properties and are studied extensively in number theory.

I hope this explanation is helpful! Let me know if you have any further questions.

'''

'''
Question: You are provided with two integers, a and b. Your task is to write a Python function that checks whether both a and b are co-prime or not.
Two numbers are said to be co-prime or mutually prime if the only positive integer that divides both of them is 1. 
The expected complexity is 
O(sqrt(max(a,b)))
'''

# Method 1: Using the Euclidean Algorithm (gcd)
# This is the simplest and most efficient way to determine if two numbers are co-prime.
# Two numbers are co-prime if their gcd (greatest common divisor) is 1.
from math import gcd

def are_coprime_gcd(a, b):
    """
    Check if two integers a and b are co-prime by finding their gcd.
    If gcd(a, b) == 1, then a and b are co-prime.
    """
    # Compute gcd of a and b using Python's built-in gcd function.
    # If gcd is 1, they are co-prime; otherwise, they are not.
    return gcd(a, b) == 1


# Method 2: Naive Factorization Approach
# This method finds the divisors of both numbers and checks if they have any common divisors other than 1.
def are_coprime_naive(a, b):
    """
    Check if two integers a and b are co-prime by finding all divisors up to sqrt(n).
    If there are no common divisors other than 1, then they are co-prime.
    """
    # Get the limit up to which we need to check for factors (sqrt(max(a, b)))
    limit = int(max(a, b) ** 0.5) + 1
    
    # Initialize sets to hold factors of a and b
    set_a = set()
    set_b = set()
    
    # Loop through possible factors up to sqrt(max(a, b))
    for i in range(2, limit):
        # Check if i is a factor of a and add it to set_a if it is
        if a % i == 0:
            set_a.add(i)
        # Check if i is a factor of b and add it to set_b if it is
        if b % i == 0:
            set_b.add(i)
    
    # Check for common factors by finding the intersection of set_a and set_b
    # If the intersection contains nothing, they are co-prime
    # We use nothing because we don't consider 1 in our code.
    # All numbers are divisible by 1.
    common_factors = set_a & set_b
    return len(common_factors) == 0


# Method 3: Manual Common Divisor Check (No `gcd`)
# In this method, we avoid using any gcd functions by directly checking for common divisors.
def are_coprime_manual(a, b):
    """
    Check if two integers a and b are co-prime by finding any common divisors manually.
    """
    # Set the limit for the loop to the square root of the smaller number
    limit = int(min(a, b) ** 0.5) + 1

    # Loop from 2 up to sqrt(min(a, b)) to check for common divisors
    for i in range(2, limit):
        # Check if i divides both a and b
        if a % i == 0 and b % i == 0:
            # If any common divisor other than 1 is found, they are not co-prime
            return False

    # If no divisors found up to sqrt(min(a, b)), check if one number divides the other
    # This handles cases where one number is prime and greater than sqrt(n)
    if a % b == 0 or b % a == 0:
        return False
    
    # If no common factors were found, a and b are co-prime
    return True

# Example usage for each method
print("Using gcd method:", are_coprime_gcd(15, 28))  # Expected output: True
print("Using naive factorization:", are_coprime_naive(15, 28))  # Expected output: True
print("Using manual divisor check:", are_coprime_manual(15, 28))  # Expected output: True


'''
Here's an analysis of the time complexities for each of the three methods:

### 1. **Method 1: Using the Euclidean Algorithm (gcd)**
- **Time Complexity**: \(O(\log(\min(a, b)))\)
- **Explanation**: The Euclidean algorithm is extremely efficient for finding the gcd of two numbers. Each step in the Euclidean algorithm reduces one of the numbers by at least half, leading to a logarithmic number of operations based on the smaller of the two numbers.

### 2. **Method 2: Naive Factorization Approach**
- **Time Complexity**: \(O(\sqrt{\max(a, b)})\)
- **Explanation**: This approach loops through numbers up to \(\sqrt{\max(a, b)}\) to find divisors, which means that it has a time complexity of \(O(\sqrt{\max(a, b)})\). For each number, it checks if it divides `a` and `b` and stores the divisors, which may add minor overhead but doesn't change the overall complexity.

### 3. **Method 3: Manual Common Divisor Check (No gcd)**
- **Time Complexity**: \(O(\sqrt{\min(a, b)})\)
- **Explanation**: This method directly checks common divisors up to \(\sqrt{\min(a, b)}\). It terminates as soon as a common divisor is found, providing early exit in cases where a divisor is found quickly. This approach does not rely on additional data structures, making it straightforward with a complexity based on the square root of the smaller number.

### Summary Table

| Method                              | Time Complexity             |
|-------------------------------------|-----------------------------|
| Euclidean Algorithm (gcd function)  | \(O(\log(\min(a, b)))\)     |
| Naive Factorization                 | \(O(\sqrt{\max(a, b)})\)    |
| Manual Common Divisor Check         | \(O(\sqrt{\min(a, b)})\)    |

Overall, the Euclidean algorithm (Method 1) is the most efficient for this problem, but each approach meets the expected complexity requirement of (O(sqrt{max(a, b)})).
'''