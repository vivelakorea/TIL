from typing import TypeVar
T = TypeVar('T')
U = TypeVar('U')


def is_equal(a: T, b: U) -> bool:
    return a == b
