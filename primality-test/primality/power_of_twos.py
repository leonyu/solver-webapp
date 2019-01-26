
import math
from typing import List


def split_by_powers_of_two(number):
    # type: (int) -> List[int]
    result = [] # type: List[int]
    if number <= 0:
        return result
    it = 2 ** int(math.log(number, 2))
    while it >= 1:
        if number >= it:
            result.insert(0, it)
            number -= it
        it = it // 2

    return result


def is_power_of_two(n):
    # type: (int) -> bool
    return (n > 0) and (2 ** int(math.log(n, 2)) == n)
