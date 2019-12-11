from typing import Iterable, Optional, List, TypeVar, Tuple

class TreeNode:
    @staticmethod
    def fromValue(value):
        # type: (Optional[int]) -> Optional[TreeNode]
        if value is None:
            return None
        return TreeNode(value)

    @staticmethod
    def toValue(node):
        # type: (Optional[TreeNode]) -> Optional[int]
        if node is None:
            return None
        return node.value

    def __init__(self, value):
        # type: (int) -> None
        self.value = value  # type: int
        self.left = None  # type: Optional[TreeNode]
        self.right = None  # type: Optional[TreeNode]


def get_bft_children(index):
    # type: (int) -> Tuple[int, int]
    return ((index * 2) + 1, (index * 2) + 2)


def from_bft(data):
    # type: (Iterable[Optional[int]]) -> Optional[TreeNode]
    result = [TreeNode.fromValue(val) for val in data]
    child_idx = 1
    for node in result:
        if node is None:
            continue
        node.left = result[child_idx]
        child_idx += 1
        node.right = result[child_idx]
        child_idx += 1

    return result[0]


def to_bft(root):
    # type: (Optional[TreeNode]) -> List[Optional[int]]
    i = 0
    result = [root]
    while i < len(result):
        current_node = result[i]
        i += 1
        if current_node is None:
            continue
        result.extend([current_node.left, current_node.right])
    return [TreeNode.toValue(node) for node in result]


def from_pre_order(data):
    # type: (Iterable[Optional[int]]) -> Optional[TreeNode]
    stack = []  # type: List[Optional[TreeNode]]
    for node in reversed([TreeNode.fromValue(val) for val in data]):
        if node is not None:
            node.left = stack.pop()
            node.right = stack.pop()
        stack.append(node)
    return stack.pop()


def to_pre_order(node):
    # type: (Optional[TreeNode]) -> List[Optional[int]]
    if node is None:
        return [None]
    result = []  # type: List[Optional[int]]
    result.append(TreeNode.toValue(node))
    result.extend(to_pre_order(node.left))
    result.extend(to_pre_order(node.right))
    return result


def to_in_order(node):
    # type: (Optional[TreeNode]) -> List[Optional[int]]
    if node is None:
        return [None]
    result = []  # type: List[Optional[int]]
    result.extend(to_in_order(node.left))
    result.append(TreeNode.toValue(node))
    result.extend(to_in_order(node.right))
    return result


def from_post_order(data):
    # type: (Iterable[Optional[int]]) -> Optional[TreeNode]
    stack = []  # type: List[Optional[TreeNode]]
    for node in [TreeNode.fromValue(val) for val in data]:
        if node is not None:
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop()


def to_post_order(node):
    # type: (Optional[TreeNode]) -> List[Optional[int]]
    if node is None:
        return [None]
    result = []  # type: List[Optional[int]]
    result.extend(to_post_order(node.left))
    result.extend(to_post_order(node.right))
    result.append(TreeNode.toValue(node))
    return result
