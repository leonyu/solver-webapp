from typing import Iterable, Optional, List


class BinaryTreeTraversal:
    def __init__(self, data=()):
        # type: (Iterable[int]) -> None
        self.data = BinaryTreeTraversal.from_bft(data)

    @staticmethod
    def flip_mapper(mapper):
        # type: (List[int]) -> List[int]
        result = [-1] * len(mapper) # type: List[int]
        for old_idx, new_idx in enumerate(mapper):
            result[new_idx] = old_idx
        return result

    @staticmethod
    def from_bft(input_data):
        # type: (Iterable[int]) -> List[int]
        return list(input_data)

    @staticmethod
    def from_pre_order(input_data):
        # type: (Iterable[int]) -> List[int]
        data = list(input_data)
        mapper = BinaryTreeTraversal(range(0, len(data))).to_pre_order()
        return [data[i] for i in BinaryTreeTraversal.flip_mapper(mapper)]

    @staticmethod
    def from_in_order(input_data):
        # type: (Iterable[int]) -> List[int]
        data = list(input_data)
        mapper = BinaryTreeTraversal(range(0, len(data))).to_in_order()
        return [data[i] for i in BinaryTreeTraversal.flip_mapper(mapper)]

    @staticmethod
    def from_post_order(input_data):
        # type: (Iterable[int]) -> List[int]
        data = list(input_data)
        mapper = BinaryTreeTraversal(range(0, len(data))).to_post_order()
        return [data[i] for i in BinaryTreeTraversal.flip_mapper(mapper)]

    @staticmethod
    def get_child_indices(idx, length):
        # type: (int) -> Iterable[int]
        result = [idx * 2 + 1, idx * 2 + 2]
        return filter(lambda x: x < length, result)

    def to_bft(self):
        # type: () -> List[int]
        result = [(0, self.data[0])]
        i = 0
        while i < len(result):
            (idx, _value) = result[i]
            for child_idx in BinaryTreeTraversal.get_child_indices(idx, len(self.data)):
                result.append((child_idx, self.data[child_idx]))
            i += 1
        return [item[1] for item in result]

    def to_pre_order(self, idx=0):
        # type: (int) -> List[int]
        output = []
        output.append(self.data[idx])
        for child_idx in BinaryTreeTraversal.get_child_indices(idx, len(self.data)):
            output.extend(self.to_pre_order(child_idx))
        return output

    def to_in_order(self, idx=0):
        # type: (int) -> List[int]
        output = []
        children = list(BinaryTreeTraversal.get_child_indices(idx, len(self.data)))
        if len(children) > 0:
            output.extend(self.to_in_order(children[0]))
        output.append(self.data[idx])
        if len(children) > 1:
            output.extend(self.to_in_order(children[1]))
        return output

    def to_post_order(self, idx=0):
        # type: (int) -> List[int]
        output = []
        for child_idx in BinaryTreeTraversal.get_child_indices(idx, len(self.data)):
            output.extend(self.to_post_order(child_idx))
        output.append(self.data[idx])
        return output
