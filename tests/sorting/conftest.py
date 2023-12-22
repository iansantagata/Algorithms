import random

import pytest
from pytest import FixtureRequest


@pytest.fixture(params=[
    pytest.param(10, id="10_elements"),
    pytest.param(100, id="100_elements"),
    pytest.param(1000, id="1000_elements")
])
def data_set_length(request: FixtureRequest) -> int:
    return request.param

@pytest.fixture()
def ordered_list(data_set_length: int) -> list:
    return list(range(data_set_length))

@pytest.fixture()
def reversed_list(ordered_list: list) -> list:
    return list(reversed(ordered_list))

@pytest.fixture()
def duplicate_list(data_set_length: int, ordered_list: list) -> list:
    return [ordered_list[0]] * data_set_length

@pytest.fixture()
def shuffled_list(ordered_list: list) -> list:
    return random.sample(ordered_list, k=len(ordered_list))

@pytest.fixture(params=[
    pytest.param({"ordered_percentage": 0.25, "shuffle_beginning": True}, id="shuffled_first_25%"),
    pytest.param({"ordered_percentage": 0.25, "shuffle_beginning": False}, id="shuffled_last_25%"),
    pytest.param({"ordered_percentage": 0.50, "shuffle_beginning": True}, id="shuffled_first_50%"),
    pytest.param({"ordered_percentage": 0.50, "shuffle_beginning": False}, id="shuffled_last_50%"),
    pytest.param({"ordered_percentage": 0.75, "shuffle_beginning": True}, id="shuffled_first_75%"),
    pytest.param({"ordered_percentage": 0.75, "shuffle_beginning": False}, id="shuffled_last_75%"),
])
def partially_ordered_list(request: FixtureRequest, ordered_list: list) -> list:

    ordered_percentage: float = request.param["ordered_percentage"]
    shuffle_beginning: bool = request.param["shuffle_beginning"]

    total_num_elements: int = len(ordered_list)
    num_ordered_elements: int = int(total_num_elements * ordered_percentage)

    if shuffle_beginning:
        ordered_sublist: list = ordered_list[-num_ordered_elements:]
        remaining_ordered_list: list = ordered_list[:-num_ordered_elements]
        shuffled_remaining_ordered_list: list = random.sample(remaining_ordered_list, k=len(remaining_ordered_list))

        return shuffled_remaining_ordered_list + ordered_sublist

    ordered_sublist: list = ordered_list[:num_ordered_elements]
    remaining_ordered_list: list = ordered_list[num_ordered_elements:]
    shuffled_remaining_ordered_list: list = random.sample(remaining_ordered_list, k=len(remaining_ordered_list))

    return ordered_sublist + shuffled_remaining_ordered_list

@pytest.fixture()
def random_list(ordered_list: list) -> list:

    random_list: list = []
    first_element = ordered_list[0]
    last_element = ordered_list[-1]

    while len(random_list) < len(ordered_list):
        random_list.append(random.randrange(first_element, last_element))

    return random_list

