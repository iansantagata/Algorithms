from sorting.bubble import sort as bubble_sort
from tests.helpers.assertions import assert_equivalent_lists


def test_sort_ordered_list(ordered_list: list) -> None:
    output: list = bubble_sort(input=ordered_list)
    expected: list = sorted(ordered_list)

    assert_equivalent_lists(output, expected)


def test_sort_revered_list(reversed_list: list) -> None:
    output: list = bubble_sort(input=reversed_list)
    expected: list = sorted(reversed_list)

    assert_equivalent_lists(output, expected)


def test_sort_duplicate_list(duplicate_list: list) -> None:
    output: list = bubble_sort(input=duplicate_list)
    expected: list = sorted(duplicate_list)

    assert_equivalent_lists(output, expected)


def test_sort_shuffled_list(shuffled_list: list) -> None:
    output: list = bubble_sort(input=shuffled_list)
    expected: list = sorted(shuffled_list)

    assert_equivalent_lists(output, expected)


def test_partially_ordered_list(partially_ordered_list: list) -> None:
    output: list = bubble_sort(input=partially_ordered_list)
    expected: list = sorted(partially_ordered_list)

    assert_equivalent_lists(output, expected)


def test_random_list(random_list: list) -> None:
    output: list = bubble_sort(input=random_list)
    expected: list = sorted(random_list)

    assert_equivalent_lists(output, expected)
