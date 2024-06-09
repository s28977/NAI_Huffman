from src.model.subtree import join
from src.priorityqueue.binary_heap import BinaryHeap
from functions import *

if __name__ == '__main__':
    with open(r'C:\Users\Jan\JetBrainsProjects\PycharmProjects\NAI_Huffman\texts\alice_in_wonderland.txt',
              encoding='utf-8') as f:
        sequence = f.read()

    symbols = map_to_symbols_list(sequence)
    subtrees = map_to_subtrees_list(symbols)
    pq = BinaryHeap(subtrees)

    while len(pq) > 1:
        left = pq.del_min()
        right = pq.del_min()
        parent = join(left, right)
        pq.insert(parent)

    root = pq.del_min()
    print(f'\n{'-' * 10}Huffman tree{'-' * 10}\n')
    print(root)

    code_dict = {}
    root.get_huffman_code_dict(code_dict)
    print(f'\n{'-' * 10}Encoding{'-' * 10}\n')
    print(code_dict)

    encoded_sequence = encode(sequence, code_dict)
    print(f'\n{'-' * 10}Original sequence{'-' * 10}\n')
    print(f'{sequence}\n')
    print(f'Size (8 bit encoding) = {(len(sequence) * 8) // 1012 + 1} KB ({len(sequence) * 8} bytes)')
    print(f'\n{'-' * 10}Encoded sequence{'-' * 10}\n')
    print(f'{encoded_sequence}\n')
    print(f'Size = {len(encoded_sequence) // (8 * 1012) + 1} KB ({len(encoded_sequence) // 8 + 1} bytes)\n')
    print(f'Encoded sequence size / Original sequence size = {(len(encoded_sequence) // 8 + 1) / (len(sequence) * 8)}')
