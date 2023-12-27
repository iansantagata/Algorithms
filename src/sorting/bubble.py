"""
Bubble Sort

More Details - https://en.wikipedia.org/wiki/Bubble_sort
"""


def sort(data: list[int]) -> list[int]:
    """
    Bubble Sort - https://en.wikipedia.org/wiki/Bubble_sort

    Memory Usage: O(1)

    Performance:
    - Worst Case: O(n²)
    - Average Case: O(n²)
    - Best Case: O(n)
    """
    num_elements: int = len(data)

    # For input with 1 or fewer elements, the list is already in order
    if num_elements <= 1:
        return data

    # Traverse through all elements
    for i in range(num_elements):
        swap_occurred: bool = False

        # The last i elements are already in their proper place
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

        if not swap_occurred:
            break

    return data
