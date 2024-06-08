import functools


@functools.total_ordering
class Symbol:
    def __init__(self, char, order, count):
        self.char = char
        self.order = order
        self.count = count

    def __eq__(self, other):
        return self.order == other.order

    def __lt__(self, other):
        return self.order < other.order
