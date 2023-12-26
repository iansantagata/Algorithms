from typing import Any

def assert_equivalent_lists(first: list[Any], second: list[Any]) -> None:
    assert len(first) == len(second)

    list_length: int = len(first)
    for index in range(list_length):
        # Want to test contents and ordering, so each index should have the same value in both lists
        assert first[index] == second[index]
