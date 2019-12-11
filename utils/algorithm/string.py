from typing import List

def find_in_lps(text, lps, c):
    # type: (str, List[int], str) -> int
    for pos in reversed(lps):
        if c == text[pos]:
            return pos
    return -1

def create_lps(text):
    # type: (str) -> List[int]
    result = [0]
    for i in range(1, len(text)):
        result.append(find_in_lps(text, result, text[i]) + 1)
    return result


def find_string(text, pattern):
    # type: (str, str) -> int
    lps = create_lps(pattern)
    pos = 0
    for i, c in enumerate(text):
        if c == pattern[pos]:
            pos += 1
            if pos == len(pattern):
                return i - len(pattern) + 1
        elif pos > 1:
            pos = lps[pos]
    return -1
