
import math

def split(number):
    result = []
    number = long(number)
    if number <= 0:
        return result
    it = 2 ** long(math.log(number, 2))
    while(it >= 1):
        if number >= it:
            result.insert(0, it)
            number -= it
        it = it / 2

    return result

def is_power_of_two(number):
    return len(split(number)) == 1