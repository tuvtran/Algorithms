public class LinkedQueueOfStrings {
	
	private Node first, last;

	private class Node {
		String item;
		Node next;
	}

	public boolean isEmpty() {
		return first == null;
	}

	public void enqueue(String item) {
		Node oldlast = last;
		last = new Node();
		last.item = item;
		last.next = null;
		if(isEmpty()) {
			// Special cases for empty queue
			first = last;
		} else {
			oldlast.next = last;
		}
	}

	public String dequeue() {
		String item = first.item;
		first = first.next;
		if(isEmpty()) {
			// Special cases for empty queue
			last = null;
		}

		return item;
	}

}
