"""
Insertion Sort https://en.wikipedia.org/wiki/Insertion_sort
"""


def sort(data: list[int]) -> list[int]:
    """
    Insertion Sort

    Performance:
    - Worst Case: O(n²)
    - Average Case: O(n²)
    - Best Case: O(n)

    Memory Usage: O(1)

    Algorithm:

    Consider the data set as consisting of two mutually exclusive subsets of data: sorted
    data first, and then unsorted data afterward.  The first element of the data set is
    considered to be sorted from the start.  The second element of the data set is defined
    as the start of the unsorted data.

    Find the first unsorted data element and store the value in that position.  Target the
    element before the stored value.  If the stored value is smaller than the target value,
    copy the target value to one spot after itself, and change the target to be the element
    before the previous target.  Continue comparing stored value vs target value until the
    stored value is not smaller then the target value.  When that happens, copy the stored
    value to this location.

    At this point, this value has been added to and sorted within the subset of sorted data.
    This also means the subset of unsorted data has decreased by one element.

    Continue this process until there are no longer any unsorted elements remaining.  The
    result will be a data set that consists entirely of the subset of sorted data.
    """
    num_elements: int = len(data)

    # For input with 1 or fewer elements, the list is already in order
    if num_elements <= 1:
        return data

    # Traverse through (almost) all elements
    # Skip only the first one which is considered already in order
    for i in range(1, num_elements):
        # Elements up to i are sorted, so grab the next value to sort
        value_to_be_sorted = data[i]

        # Start the look-back comparison (e.g. target) one position before the stored value
        j = i - 1
        while j >= 0 and value_to_be_sorted < data[j]:
            # The value is smaller than the target, so move the target data down
            # and continue the look-back comparison one spot before that target value
            data[j + 1] = data[j]
            j -= 1

        # Once the correct position has been found, insert the value to the correct position
        data[j + 1] = value_to_be_sorted

    return data
