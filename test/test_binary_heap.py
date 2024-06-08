import pytest
from copy import deepcopy

from src.priorityqueue.binary_heap import BinaryHeap

example_list = [4, 7, 2, 9, 8, 3, 1, 6, 7]
example_heap_list = [None, 2, 3, 2, 5, 3, 5, 4, 8]


def test_correct_constructor():
    pq = BinaryHeap()
    assert pq._heap_list == [None]
    assert len(pq) == 0


def test_correct_insert():
    pq = BinaryHeap()
    pq._heap_list = deepcopy(example_heap_list)
    pq.insert(1)
    assert pq._heap_list == [None, 1, 2, 2, 3, 3, 5, 4, 8, 5]


def test_correct_find_min():
    pq = BinaryHeap()
    pq._heap_list = deepcopy(example_heap_list)
    assert pq.find_min() == 2


def test_correct_del_min():
    pq = BinaryHeap()
    pq._heap_list = deepcopy(example_heap_list)
    assert pq.del_min() == 2
    assert pq._heap_list == [None, 2, 3, 4, 5, 3, 5, 8]


def test_correct_slow_construct_by_inserting_1_by_1():
    pq = BinaryHeap()
    for e in example_list:
        pq.insert(e)
    assert pq._heap_list == [None, 1, 6, 2, 7, 8, 4, 3, 9, 7]


def test_correct_fast_construct():
    pq = BinaryHeap(example_list)
    assert pq._heap_list == [None, 1, 6, 2, 7, 8, 3, 4, 9, 7]