from abc import ABC, abstractmethod


class PriorityQueue(ABC):
    @abstractmethod
    def insert(self, e):
        pass

    @abstractmethod
    def find_min(self, e):
        pass

    @abstractmethod
    def del_min(self, e):
        pass
