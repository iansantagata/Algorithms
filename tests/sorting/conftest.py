import random

import pytest
from pytest import FixtureRequest
from typing import Any


@pytest.fixture(
    params=[
        pytest.param(10, id="10_elements"),
        pytest.param(100, id="100_elements"),
        pytest.param(1000, id="1000_elements"),
    ]
)
def data_set_length(request: FixtureRequest) -> int:
    return int(request.param)


@pytest.fixture()
def ordered_list(data_set_length: int) -> list[int]:
    return list(range(data_set_length))


@pytest.fixture()
def reversed_list(ordered_list: list[int]) -> list[int]:
    return list(reversed(ordered_list))


@pytest.fixture()
def duplicate_list(data_set_length: int, ordered_list: list[int]) -> list[int]:
    return [ordered_list[0]] * data_set_length


@pytest.fixture()
def shuffled_list(ordered_list: list[int]) -> list[int]:
    return random.sample(ordered_list, k=len(ordered_list))


@pytest.fixture(
    params=[
        pytest.param(
            {"ordered_percentage": 0.25, "is_beginning_shuffled": True},
            id="shuffled_first_25%",
        ),
        pytest.param(
            {"ordered_percentage": 0.25, "is_beginning_shuffled": False},
            id="shuffled_last_25%",
        ),
        pytest.param(
            {"ordered_percentage": 0.50, "is_beginning_shuffled": True},
            id="shuffled_first_50%",
        ),
        pytest.param(
            {"ordered_percentage": 0.50, "is_beginning_shuffled": False},
            id="shuffled_last_50%",
        ),
        pytest.param(
            {"ordered_percentage": 0.75, "is_beginning_shuffled": True},
            id="shuffled_first_75%",
        ),
        pytest.param(
            {"ordered_percentage": 0.75, "is_beginning_shuffled": False},
            id="shuffled_last_75%",
        ),
    ]
)
def partially_ordered_list(request: FixtureRequest, ordered_list: list[int]) -> list[int]:
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


@pytest.fixture()
def random_list(ordered_list: list[int]) -> list[int]:
    random_list: list[int] = []
    first_element = ordered_list[0]
    last_element = ordered_list[-1]

    while len(random_list) < len(ordered_list):
        random_list.append(random.randrange(first_element, last_element))

    return random_list
