"""
Configuration file for sorting algorithm related tests.

Mostly used to setup common fixtures such as generating similar data sets sets to test
on all sorting algorithms.
"""

import random
from typing import Callable

import pytest
from pytest import FixtureRequest

from src.sorting.bubble import sort as bubble_sort
from src.sorting.insertion import sort as insertion_sort
from src.sorting.selection import sort as selection_sort
from src.sorting.merge import sort as merge_sort

SortingAlgorithmFunctionType = Callable[[list[int]], list[int]]


@pytest.fixture(
    name="data_set_length",
    params=[
        pytest.param(0, id="0 Elements"),
        pytest.param(1, id="1 Element"),
        pytest.param(10, id="10 Elements"),
        pytest.param(100, id="100 Elements"),
        pytest.param(1000, id="1000 Elements"),
    ],
)
def fixture_data_set_length(request: FixtureRequest) -> int:
    """
    Fixture representing the intended length of the data set to be generated.
    """
    return int(request.param)


@pytest.fixture(name="ordered_list")
def fixture_ordered_list(data_set_length: int) -> list[int]:
    """
    Fixture representing an ordered list of unique values of some size.
    """
    return list(range(data_set_length))


@pytest.fixture(name="reversed_list")
def fixture_reversed_list(ordered_list: list[int]) -> list[int]:
    """
    Fixture representing a reverse-ordered list of unique values of some size.
    """
    return list(reversed(ordered_list))


@pytest.fixture(name="duplicates_list")
def fixture_duplicates_list(data_set_length: int) -> list[int]:
    """
    Fixture representing a list of some size with each value as the same number.

    The value is a random non-negative integer bounded by the intended list size.
    """
    if data_set_length == 0:
        return []

    duplicates_list = [random.randint(0, data_set_length)] * data_set_length
    return duplicates_list


@pytest.fixture(name="shuffled_list")
def fixture_shuffled_list(ordered_list: list[int]) -> list[int]:
    """
    Fixture representing a fully shuffled list of some size consisting of unique values.
    """
    return random.sample(ordered_list, k=len(ordered_list))


@pytest.fixture(
    name="partially_ordered_list",
    params=[
        pytest.param(
            {"ordered_percentage": 0.25, "is_beginning_shuffled": True},
            id="Shuffled First 25%",
        ),
        pytest.param(
            {"ordered_percentage": 0.25, "is_beginning_shuffled": False},
            id="Shuffled Last 25%",
        ),
        pytest.param(
            {"ordered_percentage": 0.50, "is_beginning_shuffled": True},
            id="Shuffled First 50%",
        ),
        pytest.param(
            {"ordered_percentage": 0.50, "is_beginning_shuffled": False},
            id="Shuffled Last 50%",
        ),
        pytest.param(
            {"ordered_percentage": 0.75, "is_beginning_shuffled": True},
            id="Shuffled First 75%",
        ),
        pytest.param(
            {"ordered_percentage": 0.75, "is_beginning_shuffled": False},
            id="Shuffled Last 75%",
        ),
    ],
)
def fixture_partially_ordered_list(
    request: FixtureRequest, ordered_list: list[int]
) -> list[int]:
    """
    Fixture representing a partially ordered list containing unique values.

    The partially ordered subset is either at the beginning or end of the list,
    while the unordered subset contains shuffled values.
    """
    ordered_percentage: float = request.param["ordered_percentage"]
    is_beginning_shuffled: bool = request.param["is_beginning_shuffled"]

    total_num_elements: int = len(ordered_list)
    num_ordered_elements: int = int(total_num_elements * ordered_percentage)

    if is_beginning_shuffled:
        ordered_ending: list[int] = ordered_list[-num_ordered_elements:]
        remaining_beginning_elements: list[int] = ordered_list[:-num_ordered_elements]
        shuffled_beginning: list[int] = random.sample(
            remaining_beginning_elements, k=len(remaining_beginning_elements)
        )

        return shuffled_beginning + ordered_ending

    ordered_beginning: list[int] = ordered_list[:num_ordered_elements]
    remaining_ending_elements: list[int] = ordered_list[num_ordered_elements:]
    shuffled_ending: list[int] = random.sample(
        remaining_ending_elements, k=len(remaining_ending_elements)
    )

    return ordered_beginning + shuffled_ending


@pytest.fixture(name="random_list")
def fixture_random_list(data_set_length: int) -> list[int]:
    """
    Fixture representing an entirely random list of values (may contain duplicates).

    Each value is a random non-negative integer bounded by the intended list size.
    """
    if data_set_length == 0:
        return []

    random_list: list[int] = []
    while len(random_list) < data_set_length:
        random_value = random.randint(0, data_set_length)
        random_list.append(random_value)

    return random_list


@pytest.fixture(
    name="sorting_algorithm",
    params=[
        pytest.param(bubble_sort, id="Bubble Sort Algorithm"),
        pytest.param(insertion_sort, id="Insertion Sort Algorithm"),
        pytest.param(selection_sort, id="Selection Sort Algorithm"),
        pytest.param(merge_sort, id="Merge Sort"),
    ],
)
def fixture_sorting_algorithm(request: FixtureRequest) -> SortingAlgorithmFunctionType:
    """
    Fixture representing all the possible sorting algorithms to test.

    Each algorithm here should have the following function signature:
      - def sort(data: list[int]) -> list[int]
    """
    algorithm: SortingAlgorithmFunctionType = request.param
    return algorithm
