from src.model.subtree import Subtree, join
from src.model.symbol import Symbol
from src.priorityqueue.binary_heap import BinaryHeap


def map_to_subtrees_list(sequence):
    char_count_dict = dict()
    for char in sequence:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    subtrees = []
    for i, e in enumerate(char_count_dict.items()):
        subtrees.append(Subtree(Symbol(e[0], i, e[1])))
    return subtrees