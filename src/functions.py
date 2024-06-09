from src.model.subtree import Subtree
from src.model.symbol import Symbol


def map_to_symbols_list(sequence):
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


def map_to_subtrees_list(symbols):
    subtrees = []
    for symbol in symbols:
        subtrees.append(Subtree(symbol))
    return subtrees


def encode(sequence, code_dict):
    encoded_sequence = ''
    for char in sequence:
        encoded_sequence += code_dict[char]
    return encoded_sequence
