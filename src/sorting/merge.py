"""
Merge Sort - https://en.wikipedia.org/wiki/Merge_sort
"""

import math


def sort(data: list[int]) -> list[int]:
    """
    Merge Sort

    Performance:
    - Worst Case: O(n * log(n))
    - Average Case: O(n * log(n))
    - Best Case: O(n * log(n))

    Memory Usage: O(n)

    Algorithm:

    Start by measuring the size of the data set.  If the data set has one or fewer
    elements, return the data set as-is since it is technically sorted.

    For all other size lists, split the data set in half (or as close as possible) that
    will be referred to as the "left" subset of data and the "right" subset of data.
    Use recursion to call the same sorting function on each of the subsets of data
    (left and right).

    With these newly sorted subsets, compare the first element of the left data set with
    the first element of the right data set.  Insert the smaller value of the two onto
    the end of a new data store and remove the element from the data set it came from
    (left or right).

    Continue like this until all elements have been removed from the left and right data
    sets. The resulting data store that both subsets were merged into is now sorted.
    """
    num_elements: int = len(data)

    # Base Case #
    # For input with 1 or fewer elements, the list is already in order
    if num_elements <= 1:
        return data

    # Recursive Case #
    # Divide the data into two equal (or as near-equal as possible) sized subsets
    mid_point_index = math.floor(num_elements / 2)
    left_side = data[:mid_point_index]
    right_side = data[mid_point_index:]

    # Sort each subset using recursion
    left_side = sort(left_side)
    right_side = sort(right_side)

    # Finally, merge the two sorted subsets of data, starting when both sides
    # still have elements
    merged_data = []
    while len(left_side) != 0 and len(right_side) != 0:
        first_element_left = left_side[0]
        first_element_right = right_side[0]

        if first_element_left <= first_element_right:
            merged_data.append(first_element_left)
            left_side = left_side[1:]
        else:
            merged_data.append(first_element_right)
            right_side = right_side[1:]

    # One side still has elements, so loop through the remaining elements for each side
    # to end with a completely sorted data set
    while len(left_side) != 0:
        first_element_left = left_side[0]
        merged_data.append(first_element_left)
        left_side = left_side[1:]

    while len(right_side) != 0:
        first_element_right = right_side[0]
        merged_data.append(first_element_right)
        right_side = right_side[1:]

    return merged_data
