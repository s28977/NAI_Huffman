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

    def __repr__(self, level=0):
        indent = '\t' * level
        left_repr = self.left.__repr__(level + 1) if self.left else 'None'
        right_repr = self.right.__repr__(level + 1) if self.right else 'None'
        return (f'{self.symbol.char}, {self.count}'
                f'\n{indent}Left son: {left_repr}'
                f'\n{indent}Right son: {right_repr}')

    def get_huffman_code(self, code_dict: dict, bits=''):
        if self.right is None and self.left is None:
            code_dict[self.symbol.char] = bits
        if self.left is not None:
            self.left.get_huffman_code(code_dict, bits + '0')
        if self.right is not None:
            self.right.get_huffman_code(code_dict, bits + '1')


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


