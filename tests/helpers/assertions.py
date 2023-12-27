"""
This file contains helper functions used specifically for testing common assertions.

None of these functions or logic should not be used in non-test use cases.

These functions are here to reduce testing duplication and utilize similar logic in
tests wherever possible, especially when asserting something is required.
"""

from typing import Any


def assert_equivalent_lists(first: list[Any], second: list[Any]) -> None:
    """
    A helper function that asserts that a list with any primitive contents
    (string, int, etc) is equivalent to another list.

    Equivalency here means that the lists:
    - Have the same number of elements
    - Have elements in the same order
    - Have elements that are equal to one another (this is why primitives are required)
    """
    assert len(first) == len(second)

    list_length: int = len(first)
    for index in range(list_length):
        # Want to test contents and ordering, so each index should have the same value
        # in both lists
        assert first[index] == second[index]
