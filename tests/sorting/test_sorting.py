# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from typing import Callable

from tests.helpers.assertions import assert_equivalent_lists

SortingAlgorithmFunctionType = Callable[[list[int]], list[int]]


def test_sort_ordered_list(
    ordered_list: list[int], sorting_algorithm: SortingAlgorithmFunctionType
) -> None:
    output: list[int] = sorting_algorithm(ordered_list)
    expected: list[int] = sorted(ordered_list)

    assert_equivalent_lists(output, expected)


def test_sort_reversed_list(
    reversed_list: list[int], sorting_algorithm: SortingAlgorithmFunctionType
) -> None:
    output: list[int] = sorting_algorithm(reversed_list)
    expected: list[int] = sorted(reversed_list)

    assert_equivalent_lists(output, expected)


def test_sort_duplicates_list(
    duplicates_list: list[int], sorting_algorithm: SortingAlgorithmFunctionType
) -> None:
    output: list[int] = sorting_algorithm(duplicates_list)
    expected: list[int] = sorted(duplicates_list)

    assert_equivalent_lists(output, expected)


def test_sort_shuffled_list(
    shuffled_list: list[int], sorting_algorithm: SortingAlgorithmFunctionType
) -> None:
    output: list[int] = sorting_algorithm(shuffled_list)
    expected: list[int] = sorted(shuffled_list)

    assert_equivalent_lists(output, expected)


def test_partially_ordered_list(
    partially_ordered_list: list[int], sorting_algorithm: SortingAlgorithmFunctionType
) -> None:
    output: list[int] = sorting_algorithm(partially_ordered_list)
    expected: list[int] = sorted(partially_ordered_list)

    assert_equivalent_lists(output, expected)


def test_random_list(
    random_list: list[int], sorting_algorithm: SortingAlgorithmFunctionType
) -> None:
    output: list[int] = sorting_algorithm(random_list)
    expected: list[int] = sorted(random_list)

    assert_equivalent_lists(output, expected)
