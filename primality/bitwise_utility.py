
def get_bits(target):
    result = []
    value = target
    part = value & ~(value - 1)
    while part != 0:
        result.append(part)
        value -= part
        part = value & ~(value - 1)
    return result
