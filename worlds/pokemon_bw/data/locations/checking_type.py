from typing import Callable


def flag_at_bit_0(value: int) -> bool:
    return value & 1 == 1


def flag_at_bit_1(value: int) -> bool:
    return value & 2 == 2


def flag_at_bit_2(value: int) -> bool:
    return value & 4 == 4


def flag_at_bit_3(value: int) -> bool:
    return value & 8 == 8


def flag_at_bit_4(value: int) -> bool:
    return value & 16 == 16


def flag_at_bit_5(value: int) -> bool:
    return value & 32 == 32


def flag_at_bit_6(value: int) -> bool:
    return value & 64 == 64


def flag_at_bit_7(value: int) -> bool:
    return value & 128 == 128


def value_equals(comparison: int) -> Callable[[int], bool]:
    return lambda value: value == comparison


def value_less_than(comparison: int) -> Callable[[int], bool]:
    return lambda value: value < comparison


def value_greater_than(comparison: int) -> Callable[[int], bool]:
    return lambda value: value > comparison
