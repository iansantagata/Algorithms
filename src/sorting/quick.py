"""
Quick Sort - https://en.wikipedia.org/wiki/Quicksort
"""

import math


def sort(data: list[int]) -> list[int]:
    """
    Quick Sort

    Performance:
    - Worst Case: O(n * log(n))
    - Average Case: O(n * log(n))
    - Best Case: O(n²)

    Memory Usage: O(log(n))

    Algorithm:

    Given a data set, select an element to use as a "pivot".  The choice of which
    element to use as the pivot can be random if desired, but common non-complex
    choices are the first, last, or median element of the data set.  This pivot
    element will be used to filter other elements in the data set into two sub-sets,
    one with values less than the pivot and the other with values greater than or
    equal to the pivot.

    Setup two pointers (i.e. indexes), one pointing to the first (i.e. left-most)
    spot in the data set and the other at the last (right-most) spot in the data set.
    As long as the pointers do not point to the same space or cross over each other,
    continue to check the value in each pointer and compare against the pivot value.

    If the value in the left pointer position is less than the pivot value, move the
    left pointer one space to the right.  Similarly, if the value in the right pointer
    position is greater than the pivot value, move the right pointer one space to the
    left.  If neither the pointers moved and the values in the pointers are the same,
    move the pointer on the left one space to the right.  If none of the indexes moved,
    swap the values that the pointers are pointing to.

    Once the pointers either point to the same space or cross over each other, the
    data set has been split into a left partition, the pivot value, and a right
    partition.  The left partition contains unsorted values that are each less than
    the pivot value.  The right partition contains unsorted values that are each greater
    than or equal to the pivot value.  The space that the right pointer is pointing to
    contains the pivot value used.

    With each separated partition, recursively call the same sorting function that will
    once again setup two pointers and create sub-partitions on each subset of the data.
    With the results from the sortation of the left partition, append the pivot value,
    then append the results of the sortation of the right partition.

    The result returned will be an ordered data set from recursive sorting of partitions.
    """
    num_elements: int = len(data)

    # For input with 1 or fewer elements, the list is already in order
    if num_elements <= 1:
        return data

    # Choose a pivot value (using median indexed element here)
    pivot_index = math.floor(num_elements / 2)
    pivot_value = data[pivot_index]

    # Use double indices to track elements on both sides of the array for swapping purposes
    left_index = 0
    right_index = num_elements - 1

    # Traverse through all elements, comparing against the pivot
    while left_index < right_index:

        # Move the left index to the right if the value is on the correct side of the pivot
        left_value = data[left_index]
        if left_value < pivot_value:
            left_index += 1
            continue

        # Move the right index to the left if the value is on the correct side of the pivot
        right_value = data[right_index]
        if right_value > pivot_value:
            right_index -= 1
            continue

        # Move the left index to the right if the values since no swap should be performed
        # Avoids infinite recursion when there are duplicate values
        if left_value == right_value:
            left_index += 1
            continue

        # When both elements are on the wrong side, swap them
        data[left_index] = right_value
        data[right_index] = left_value

    # Keep track of where the pivot has moved to and separate out partitions
    pivot_index = right_index
    left_partition = data[0:pivot_index]
    pivot_partition = [
        data[pivot_index]
    ]  # Split the pivot out to avoid infinite recursion
    right_partition = data[pivot_index + 1 :]

    # Recursively sort the partitions and return the sorted result
    return sort(left_partition) + pivot_partition + sort(right_partition)
