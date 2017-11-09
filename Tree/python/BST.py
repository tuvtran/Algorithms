from typing import TypeVar, Generic, Any
from abc import ABCMeta, abstractmethod
import unittest


class Comparable(metaclass=ABCMeta):

    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __gt__(self, other: Any) -> bool: ...

    def __le__(self, other: Any) -> bool:
        return not self > other

    def __ge__(self, other: Any) -> bool:
        return not self < other


K = TypeVar('K', bound=Comparable)
V = TypeVar('V')


class TreeNode(Generic[K, V]):

    def __init__(
        self, key: K, value: V,
        left_child: 'TreeNode[K, V]' = None,
        right_child: 'TreeNode[K, V]' = None
    ) -> None:
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BST(Generic[K, V]):

    def __init__(self):
        self.root: TreeNode[K, V] = None
        self.size = 0

    def put(self, key: K, value: V) -> None:
        """
        Insert a new key, value pair into the BST
        """
        self.root = self._put(key, value, self.root)

    def _put(self, key: K, value: V, node: TreeNode[K, V]) -> TreeNode:
        """
        Helper method for put()
        """
        if node is None:
            return TreeNode(key, value)

        if key > node.key:
            node.right_child = self._put(key, value, node.right_child)
        elif key < node.key:
            node.left_child = self._put(key, value, node.left_child)
        else:
            node.value = value

        return node

    def get(self, key: K) -> V:
        """
        Get value from a key
        """
        return self._get(key, self.root)

    def _get(self, key: K, node: TreeNode[K, V]) -> V:
        """
        Helper method for get()
        """
        if node is None:
            return None

        if key > node.key:
            return self._get(key, node.right_child)
        elif key < node.key:
            return self._get(key, node.left_child)
        else:
            return node.value

    def floor(self, key: K) -> K:
        """
        Return the maximum key that is less than or equal to a key
        """
        x: TreeNode = self._floor(key, self.root)
        return None if x is None else x.key

    def _floor(self, key: K, node: TreeNode[K, V]) -> TreeNode:
        """
        Helper method for floor()
        """
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._floor(key, node.left_child)

        t: TreeNode = self._floor(key, node.right_child)
        return node if t is None else t

    def ceil(self, key: K) -> K:
        """
        Return the minimum key that is greater than or equal to a key
        """
        x: TreeNode = self._ceil(key, self.root)
        return None if x is None else x.key

    def _ceil(self, key: K, node: TreeNode[K, V]):
        """
        Helper method for ceil()
        """
        if node is None:
            return None

        if key == node.key:
            return node

        if key > node.key:
            return self._ceil(key, node.right_child)

        t: TreeNode = self._ceil(key, node.left_child)
        return node if t is None else t


class TestBST(unittest.TestCase):

    def test_insert(self):
        bst = BST()
        bst.put(10, None)
        self.assertEqual(bst.root.key, 10)


if __name__ == "__main__":
    unittest.main()
