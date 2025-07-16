def merge_n_sorted_lists(arr: list[list[int]]) -> list[int]:
    """
    Merges n sorted lists into a single sorted list.

    Args:
        arr: A list of sorted lists.

    Returns:
        A single sorted list containing all elements from the input lists.
    """

    def merge(left, right):
        """
        Merges two sorted lists into a single sorted list.

        Args:
            left: A sorted list.
            right: A sorted list.

        Returns:
            A single sorted list containing all elements from the input lists.
        """

        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    if not arr:
        return []

    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = merge_n_sorted_lists(arr[:mid])
    right_half = merge_n_sorted_lists(arr[mid:])

    return merge(left_half, right_half)