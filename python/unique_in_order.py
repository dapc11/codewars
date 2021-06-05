import itertools


def unique_in_order(iterable):
    return list(i for i, _ in itertools.groupby(iterable))


assert (unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'])
