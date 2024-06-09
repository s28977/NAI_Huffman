from src.model.subtree import Subtree, join
from src.model.symbol import Symbol
from src.priorityqueue.binary_heap import BinaryHeap


def map_to_symbols(sequence):
    char_count_dict = dict()
    for char in sequence:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    symbols = []
    for i, e in enumerate(char_count_dict.items()):
        symbols.append(Symbol(e[0], i, e[1]))
    return symbols


def map_to_subtrees(symbols):
    subtrees = []
    for symbol in symbols:
        subtrees.append(Subtree(symbol))
    return subtrees


def encode(sequence, code_dict):
    encoded_sequence = ''
    for char in sequence:
        encoded_sequence += code_dict[char]
    return encoded_sequence


sequence = 'aabcedef'
symbols = map_to_symbols(sequence)
subtrees = map_to_subtrees(symbols)
pq = BinaryHeap(subtrees)

while len(pq) > 1:
    left = pq.del_min()
    right = pq.del_min()
    parent = join(left, right)
    pq.insert(parent)

root = pq.del_min()
print(root)

code_dict = {}
root.get_huffman_code(code_dict)
print(code_dict)

encoded_sequence = encode(sequence, code_dict)
print(f'{sequence} = {encoded_sequence}')
