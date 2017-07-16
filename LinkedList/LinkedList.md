# Linked List

## Properties:
- `Node<T>`:
    - `T data`
    - `Node<T> value`
    - `Node<T> prev` (for doubly linked list)
- `LinkedList<T>`:
    - `Node<T> head`
    - `Node<T> tail`
    - `int size`

## Methods:
- `int size()`: return size of linked list
- `boolean is_empty()`: return `true` if empty
- `T get(int index)`: return value at `index`
- `void push_front(T value)`
- `T pop_front()`
- `void push_back(T value)`
- `T pop_back()`
- `T front()`: get the front of linked list
- `T back()`: get the back of linked list
- `boolean find(T value)`: is value in the list?
- `void add_before(Node<T> node, T value)`
- `void add_after(Node<t> node, T value)`
- `void erase(int index)`: remove node at given index
- `void remove_value(T value)`: remove the first node in the list with given value