"""
Selection Sort - https://en.wikipedia.org/wiki/Selection_sort
"""


def sort(data: list[int]) -> list[int]:
    """
    Insertion Sort

    Performance:
    - Worst Case: O(n²)
    - Average Case: O(n²)
    - Best Case: O(n²)

    Memory Usage: O(1)

    Algorithm:

    Consider the data set as consisting of two mutually exclusive subsets of data:
    sorted data first, and then unsorted data afterward.  No elements are considered
    to be in the sorted data subset at the start.

    Find the first unsorted data element and store the value in that position.  Moving
    through the unsorted data elements, find the lowest value and its position.  Once
    found, swap the value with the element in the first unsorted data element's position.

    At this point, this value has been added to and sorted within the subset of sorted
    data.  This also means the subset of unsorted data has decreased by one element.

    Continue this process until there are no longer any unsorted elements remaining.
    The result will be a data set that consists entirely of the subset of sorted data.
    """
    num_elements: int = len(data)

    # For input with 1 or fewer elements, the list is already in order
    if num_elements <= 1:
        return data

    # Traverse through all elements, trying to find the smallest value each time
    for i in range(0, num_elements):
        # Elements up to i are already sorted, so grab the first unsorted one
        # and assume it is the minimum unsorted value for now
        minimum_value = data[i]
        minimum_index = i

        # Traverse the reset of the elements afterward, finding the actual minimum
        # value and position among all unsorted elements
        for j in range(i + 1, num_elements):
            if data[j] < minimum_value:
                # Found a new minimum value, so store it and remember its index
                minimum_value = data[j]
                minimum_index = j

        # Swap the minimum value found with the first unsorted value's position,
        # adding to the subset of sorted data
        if minimum_index != i:
            data[j] = data[i]
            data[i] = minimum_value

    return data
