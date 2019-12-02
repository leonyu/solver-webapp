
from typing import Iterable


class MaxHeap:
    def __init__(self, data=()):
        # type: (Iterable[init]) -> None
        self.data = list(data)
        last_parent = int(len(self.data) / 2) - 1
        for i in range(last_parent, -1, -1):
            self.heapify(i)

    def swap(self, left, right):
        # type: (int, int) -> None
        temp = self.data[left]
        self.data[left] = self.data[right]
        self.data[right] = temp

    def pop(self):
        # type: () -> int
        result = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify(0)
        return result

    def peak(self):
        return self.data[0]

    def get_larger_branch(self, idx):
        length = len(self.data)
        left = 2 * idx + 1
        right = 2 * idx + 2
        if length <= left:  # no children
            return None
        if length <= right:  # 1 child
            return left
        if self.data[left] > self.data[right]:
            return left
        return right

    def heapify(self, idx):
        # type: (int) -> None
        large_side = self.get_larger_branch(idx)
        if large_side is None:
            return
        if self.data[large_side] > self.data[idx]:
            self.swap(large_side, idx)
            self.heapify(large_side)
