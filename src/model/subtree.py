import functools
import re

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
        indent_marker = '|'
        element_marker = '-'
        indent = f'{indent_marker}\t' * level
        message = f'{indent}{element_marker} count: {self.count}'
        if self.left is None and self.right is None:
            if re.fullmatch(r'\s', self.symbol.char):
                message += f', white character: {ord(self.symbol.char)} (decimal unicode code)'
            else:
                message += f', character: {self.symbol.char}'
        if self.left is not None:
            message += (f'\n{indent}{element_marker} left child:' +
                        f'\n{self.left.__repr__(level + 1)}')
        if self.right is not None:
            message += (f'\n{indent}{element_marker} right child:' +
                        f'\n{self.right.__repr__(level + 1)}')
        return message

    def get_huffman_code_dict(self, code_dict: dict, bits=''):
        if self.left is None and self.right is None:
            if re.fullmatch(r'\s', self.symbol.char):
                char = f'U+{ord(self.symbol.char)}'
            else:
                char = self.symbol.char
            code_dict[char] = bits
        if self.left is not None:
            self.left.get_huffman_code_dict(code_dict, bits + '0')
        if self.right is not None:
            self.right.get_huffman_code_dict(code_dict, bits + '1')


# static methods:
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
