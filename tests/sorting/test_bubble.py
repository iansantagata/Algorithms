# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from sorting.bubble import sort as bubble_sort
from tests.helpers.assertions import assert_equivalent_lists


def test_sort_ordered_list(ordered_list: list[int]) -> None:
    output: list[int] = bubble_sort(data=ordered_list)
    expected: list[int] = sorted(ordered_list)

    assert_equivalent_lists(output, expected)


def test_sort_revered_list(reversed_list: list[int]) -> None:
    output: list[int] = bubble_sort(data=reversed_list)
    expected: list[int] = sorted(reversed_list)

    assert_equivalent_lists(output, expected)


def test_sort_duplicate_list(duplicate_list: list[int]) -> None:
    output: list[int] = bubble_sort(data=duplicate_list)
    expected: list[int] = sorted(duplicate_list)

    assert_equivalent_lists(output, expected)


def test_sort_shuffled_list(shuffled_list: list[int]) -> None:
    output: list[int] = bubble_sort(data=shuffled_list)
    expected: list[int] = sorted(shuffled_list)

    assert_equivalent_lists(output, expected)


def test_partially_ordered_list(partially_ordered_list: list[int]) -> None:
    output: list[int] = bubble_sort(data=partially_ordered_list)
    expected: list[int] = sorted(partially_ordered_list)

    assert_equivalent_lists(output, expected)


def test_random_list(random_list: list[int]) -> None:
    output: list[int] = bubble_sort(data=random_list)
    expected: list[int] = sorted(random_list)

    assert_equivalent_lists(output, expected)
