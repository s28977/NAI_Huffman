import functools

from .symbol import Symbol


@functools.total_ordering
class Subtree:

    def __init__(self, symbol: Symbol = None):
        if symbol is not None:
            self.symbol = symbol
            self.count = symbol.count
        else:
            self.symbol = None
            self.count = None
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.count == other.count and self.symbol == other.symbol

    def __lt__(self, other):
        if self.count == other.count:
            return self.symbol < other.symbol
        else:
            return self.count < other.count

    def __repr__(self):
        return (f'{self.symbol.char}, {self.symbol.order}, {self.count}'
                f'\nLeft son: {str(self.left)}'
                f'\nRight son: {str(self.right)}')


def join(left: Subtree, right: Subtree):
    parent = Subtree()
    parent.left = left
    parent.right = right
    parent.count = left.count + right.count
    if left.symbol < right.symbol:
        parent.symbol = left.symbol
    else:
        parent.symbol = right.symbol
    return parent
