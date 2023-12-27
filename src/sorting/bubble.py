"""
Bubble Sort https://en.wikipedia.org/wiki/Bubble_sort
"""


def sort(data: list[int]) -> list[int]:
    """
    Bubble Sort - https://en.wikipedia.org/wiki/Bubble_sort

    Performance:
    - Worst Case: O(n²)
    - Average Case: O(n²)
    - Best Case: O(n)

    Memory Usage: O(1)

    Algorithm:

    Basically, starting with the first element and considering pairs of elements, move
    the bigger element of the pair toward the end by swapping the values.

    Continue like this, moving down the list, pair by pair, until the end of the list is
    reached.  At this point, the last element of the list is necessarily the greatest
    value in the whole list.

    Start again with the first element, and compare and swap pairs in a similar manner
    again until either no swaps have been made or the part of the list that
    has been sorted is reached.
    """
    num_elements: int = len(data)

    # For input with 1 or fewer elements, the list is already in order
    if num_elements <= 1:
        return data

    # Traverse through all elements
    for i in range(num_elements):
        swap_occurred: bool = False

        # The last i elements are already in their proper place, so we can stop at that
        # point rather than needing to check every element again.
        for j in range(1, num_elements - i):
            # Compare one earlier element to the current element and switch the values
            # if they are out of order
            if data[j - 1] > data[j]:
                # Use temporary values to switch the two variables so we do not
                # accidentally overwrite and lose either one
                temp_current_value = data[j]
                temp_previous_value = data[j - 1]

                data[j - 1] = temp_current_value
                data[j] = temp_previous_value

                swap_occurred = True

        # If we did not swap at all from i through the end of the unsorted portion of
        # the list, then we know that the list is now entirely sorted!
        if not swap_occurred:
            break

    return data
