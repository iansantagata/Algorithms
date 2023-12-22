import pytest
from sorting.bubble import sort
from tests.helpers.assertions import assert_equivalent_lists

from typing import NoReturn


def test_sort_ordered_list(ordered_list: list) -> NoReturn:
    
    output: list = sort(input=ordered_list)
    expected: list = ordered_list

    assert_equivalent_lists(output, expected)

def test_sort_revered_list(reversed_list: list, ordered_list: list) -> NoReturn:

    output: list = sort(input=reversed_list)
    expected: list = ordered_list

    assert_equivalent_lists(output, expected)

def test_sort_duplicate_list(duplicate_list: list) -> NoReturn:

    output: list = sort(input=duplicate_list)
    # Cannot use ordered_list as expected output here because it was not fully used to build the duplicate list
    expected: list = sorted(duplicate_list)

    assert_equivalent_lists(output, expected)

def test_sort_shuffled_list(shuffled_list: list, ordered_list: list) -> NoReturn:

    output: list = sort(input=shuffled_list)
    expected: list = ordered_list

    assert_equivalent_lists(output, expected)

def test_partially_ordered_list(partially_ordered_list: list, ordered_list: list) -> NoReturn:

    output: list = sort(input=partially_ordered_list)
    expected: list = ordered_list

    assert_equivalent_lists(output, expected)

def test_random_list(random_list: list) -> NoReturn:

    output: list = sort(input=random_list)
    # Cannot use ordered_list as expected output here because it was not fully used to build the random list
    expected: list = sorted(random_list)

    assert_equivalent_lists(output, expected)