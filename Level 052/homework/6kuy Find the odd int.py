def find_it(seq):
    result = 0
    for number in seq:
        result ^= number
    return result