from .priority_queue import PriorityQueue


class BinaryHeap(PriorityQueue):
    def __init__(self, heap_list=None):
        self._heap_list = [None]
        # fast construct
        if heap_list is not None:
            self._heap_list.extend(heap_list)
            for i in range(len(heap_list) // 2, 0, -1):
                self._downheap(i)

    def __len__(self):
        return len(self._heap_list) - 1

    def find_min(self):
        return self._heap_list[1]

    def del_min(self):
        res = self._heap_list[1]
        self._heap_list[1] = self._heap_list.pop()
        self._downheap(1)
        return res

    def insert(self, e):
        self._heap_list.append(e)
        i = len(self._heap_list) - 1
        self._upheap(i)

    def _upheap(self, i):
        e = self._heap_list[i]
        parent = i // 2
        while parent > 0 and self._heap_list[parent] > e:
            self._heap_list[i] = self._heap_list[parent]
            i = parent
            parent //= 2
        self._heap_list[i] = e

    def _downheap(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        min = i
        if left_child <= len(self) and self._heap_list[left_child] < self._heap_list[min]:
            min = left_child
        if right_child <= len(self) and self._heap_list[right_child] < self._heap_list[min]:
            min = right_child
        self._heap_list[i], self._heap_list[min] = self._heap_list[min], self._heap_list[i]
        while i != min:
            i = min
            left_child = i * 2
            right_child = i * 2 + 1
            if left_child <= len(self) and self._heap_list[left_child] < self._heap_list[min]:
                min = left_child
            if right_child <= len(self) and self._heap_list[right_child] < self._heap_list[min]:
                min = right_child
            self._heap_list[i], self._heap_list[min] = self._heap_list[min], self._heap_list[i]
