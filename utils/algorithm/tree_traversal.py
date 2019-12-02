from typing import Iterable, Optional, List

class TreeTraversal:
    def __init__(self, data=()):
        # type: (Iterable[int]) -> None
        self.data = list(data)

    def get_child_indices(self, idx):
        # type: (int) -> Iterable[int]
        result = [idx * 2 + 1, idx * 2 + 2]
        return filter(lambda x: x < len(self.data), result)

    def bfs(self):
        # type: () -> List[int]
        result = [(0, self.data[0])]
        i = 0
        while i < len(result):
            (idx, _value) = result[i]
            for child_idx in self.get_child_indices(idx):
                result.append((child_idx, self.data[child_idx]))
            i += 1
        return [item[1] for item in result]

    def pre_order(self, idx=0):
        # type: (int) -> List[int]
        output = []
        output.append(self.data[idx])
        for child_idx in self.get_child_indices(idx):
            output.extend(self.pre_order(child_idx))
        return output

    def in_order(self, idx=0):
        # type: (int) -> List[int]
        output = []
        children = list(self.get_child_indices(idx))
        if len(children) > 0:
            output.extend(self.in_order(children[0]))
        output.append(self.data[idx])
        if len(children) > 1:
            output.extend(self.in_order(children[1]))
        return output

    def post_order(self, idx=0):
        # type: (int) -> List[int]
        output = []
        for child_idx in self.get_child_indices(idx):
            output.extend(self.post_order(child_idx))
        output.append(self.data[idx])
        return output
