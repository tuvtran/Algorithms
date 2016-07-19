/*
	This is a singly non-circular linked list with sentinel node
*/
public class SLinkedList<T> {
	private class Node {
		T item;
		Node next;

		public Node(T item, Node next) {
			this.item = item;
			this.next = next;
		}
	}

	private Node head;
	private int size;

	// Constructor for empty list
	public SLinkedList() {
		size = 0;
		head = new Node(null, null);
	}

	// Constructor for non-empty list
	public SLinkedList(T item) {
		size = 1;
		head = new Node(null, null);
		head.next = new Node(item, null);
	}

	public void insertHead(T item) {
		size += 1;
		head.next = new Node(item, head.next);
	} 

	public T getHead() {
		return head.next.item;
	}

	public void deleteHead() {
		if (head.next != null) {
			size -= 1;
			head.next = head.next.next;
		} else {
			System.out.println("The list is already empty!");
		}
	}

	public void insertBack(T item) {
		size += 1;
		Node oldBack = this.getBack();
		oldBack.next = new Node(item, null);
	}

	public Node getBack() {
		Node current = head;
		while (current.next != null) {
			current = current.next;
		}

		return current;
	}

	public int getSize() {
		return size;
	}

	public String toString() {
		return head.next.item + "---" + head.next.next;
	}

	public static void main(String args[]) {
		SLinkedList<Integer> s = new SLinkedList<Integer>(10);
		s.insertHead(0);
		s.insertHead(-10);
		s.insertBack(20);
		s.insertBack(30);
		s.insertBack(40);
		s.deleteHead();
		System.out.println(s);
	}
}