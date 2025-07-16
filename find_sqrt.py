def mySqrt(x: int) -> int:
    # Check if x is 0 or 1 because in these cases, the square root is the number itself
    # For example, sqrt(0) = 0 and sqrt(1) = 1, so we return x directly.
    if x < 2:
        return x  

    # Define the binary search range:
    # - Start `left` at 2 because we know x is at least 2 here.
    # - Set `right` to x // 2. Any integer square root of x will be <= x / 2 for x >= 2.
    left, right = 2, x // 2  
    
    # Start the binary search loop.
    while left <= right:
        # Calculate the midpoint to split the search range.
        mid = left + (right - left) // 2

        # Square `mid` to compare it with `x`.
        squared = mid * mid

        # Case 1: If `mid * mid` equals `x`, we have found the square root.
        if squared == x:
            return mid

        # Case 2: If `mid * mid` is less than `x`, it means `mid` might be smaller than the
        # integer square root. Therefore, we move `left` to mid + 1 to search in the upper half.
        elif squared < x:
            left = mid + 1

        # Case 3: If `mid * mid` is more than `x`, `mid` is too large.
        # Adjust `right` to mid - 1 to search in the lower half.
        else:
            right = mid - 1

    # When the loop exits, `right` will point to the largest integer whose square is <= x.
    # So, we return `right` as it represents the integer square root of x.
    return right  


