from typing import Generic, TypeVar, Any, Sized    # noqa
import unittest

T = TypeVar('T')


class Node(Generic[T]):

    def __init__(self, value: T, next_node=None, prev_node=None) -> None:
        self.val = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.val)


class LinkedList(Generic[T], Sized):

    def __init__(self) -> None:
        self.head = None    # type: Any
        self.tail = None    # type: Any
        self.size = 0

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer
            pointer = pointer.next_node

    def __str__(self):
        values = [str(x) for x in self]
        return '-->'.join(values)

    def __len__(self):
        return self.size

    @classmethod
    def from_list(cls, li: list):
        ll = cls()      # type: LinkedList[T]
        for e in li:
            ll.push_back(e)

        return ll

    def push_front(self, val: T) -> None:
        if not self.head:
            self.tail = self.head = Node(val)
        else:
            self.head = Node(val, self.head)
        self.size += 1

    def push_back(self, val: T) -> None:
        if not self.head:
            self.tail = self.head = Node(val)
        else:
            self.tail.next_node = Node(val)
            self.tail = self.tail.next_node
        self.size += 1

    def pop_front(self) -> T:
        if not self.head:
            raise Exception("List is empty!")
        value = self.head.val
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def pop_back(self) -> T:
        if not self.head:
            raise Exception("List is empty!")
        value = self.tail.val
        pointer = self.head
        while pointer.next_node and pointer.next_node.next_node:
            pointer = pointer.next_node
        if not pointer.next_node:
            self.head = None
            self.tail = None
        else:
            self.tail = pointer
            pointer.next_node = None
        self.size -= 1
        return value

    def delete(self, n: T) -> None:
        if not self.head:
            raise Exception("List is empty!")

        pointer = self.head
        while pointer.next_node:
            if pointer.next_node.val == n:
                pointer.next_node = pointer.next_node.next_node
                break
            pointer = pointer.next_node

        self.size -= 1
        self.tail = pointer


class LinkedListTest(unittest.TestCase):

    def test_push_front(self):
        ll = LinkedList()

        # Adding first item
        ll.push_front("First value")
        self.assertEqual(ll.size, 1)
        self.assertEqual(str(ll.head), "First value")
        self.assertEqual(str(ll.tail), "First value")

        # Adding second item before the first item
        ll.push_front("First first value")
        self.assertEqual(ll.size, 2)
        self.assertEqual(str(ll.head), "First first value")
        self.assertEqual(str(ll.head.next_node), "First value")
        self.assertEqual(str(ll.tail), "First value")

    def test_push_back(self):
        ll = LinkedList()

        # Adding first item
        ll.push_back("First")
        self.assertEqual(ll.size, 1)
        self.assertEqual(str(ll.head), "First")
        self.assertEqual(str(ll.tail), "First")

        # Adding second item
        ll.push_back("Second")
        self.assertEqual(ll.size, 2)
        self.assertEqual(str(ll.head), "First")
        self.assertEqual(str(ll.head.next_node), "Second")
        self.assertEqual(str(ll.tail), "Second")

    def test_pop_front(self):
        ll = LinkedList()

        # Adding items to the list: 1 -> 2 -> 3
        for i in range(1, 4):
            ll.push_back(i)

        # Remove the first item
        self.assertEqual(ll.pop_front(), 1)
        self.assertEqual(ll.size, 2)
        self.assertEqual(str(ll.head), '2')

        # Remove the next item
        self.assertEqual(ll.pop_front(), 2)
        self.assertEqual(str(ll.head), '3')
        self.assertEqual(str(ll.head), str(ll.tail))
        self.assertEqual(ll.size, 1)

        # Remove the last item
        self.assertEqual(ll.pop_front(), 3)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.size, 0)

    def test_pop_back(self):
        ll = LinkedList()

        for i in range(1, 4):
            ll.push_back(i)

        # Remove the last item
        self.assertEqual(ll.pop_back(), 3)
        self.assertEqual(ll.size, 2)
        self.assertEqual(str(ll.tail), '2')

        # Remove the next item
        self.assertEqual(ll.pop_back(), 2)
        self.assertEqual(str(ll.tail), '1')
        self.assertEqual(str(ll.head), str(ll.head))
        self.assertEqual(ll.size, 1)

        # Remove the first item
        self.assertEqual(ll.pop_front(), 1)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.size, 0)

    def test_delete(self):
        ll = LinkedList()

        for i in range(1, 5):
            ll.push_back(i)

        ll.delete(2)
        self.assertEqual(ll.size, 3)
        self.assertNotIn('2', str(ll))

        ll.push_front(0)
        self.assertEqual(ll.size, 4)
        ll.delete(4)
        self.assertEqual(ll.size, 3)
        self.assertEqual(str(ll.tail), '3')

        with self.assertRaises(Exception):
            empty_ll = LinkedList()
            empty_ll.delete(99)

    def test_iter(self):
        ll = LinkedList()

        for i in range(10):
            ll.push_back(i)

        self.assertListEqual([str(x) for x in ll], list(map(str, range(10))))

    def test_str(self):
        ll = LinkedList()

        for i in range(10):
            ll.push_back(i)

        self.assertEqual(str(ll), '-->'.join(list(map(str, range(10)))))

    def test_from_list(self):
        values = [12, 45, 65, 78, 34, 90]
        self.assertEqual(
            str(LinkedList.from_list(values)),
            "-->".join(list(map(str, values)))
        )


if __name__ == "__main__":
    unittest.main()
