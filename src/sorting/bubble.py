"""
Bubble Sort - https://en.wikipedia.org/wiki/Bubble_sort
"""
from typing import NoReturn


def sort(input: list) -> list:
    num_elements: int = len(input)

    # For input with 1 or fewer elements, the list is already in order
    if num_elements <= 1:
        return input

    # Traverse through all elements
    for i in range(num_elements):
        swap_occurred: bool = False

        # The last i elements are already in their proper place
        for j in range(1, num_elements - i):
            # Compare one earlier element to the current element and switch the values if they are out of order
            if input[j - 1] > input[j]:
                # Use temporary values to switch the two variables so we do not accidentally overwrite and lose either one
                temp_current_value = input[j]
                temp_previous_value = input[j - 1]

                input[j - 1] = temp_current_value
                input[j] = temp_previous_value

                swap_occurred = True

        if not swap_occurred:
            break

    return input
