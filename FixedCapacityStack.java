public class FixedCapacityStack<Item> {

	private Item[] s;
	private int N = 0;

	public FixedCapacityStack(int capacity) {
		// s = new Item[capacity];
		s = (Item[]) new Object[capacity]; // casting because Java does not support initialing generic array
	}

	public boolean isEmpty() {
		return N == 0;
	}

	public void push(Item item) {
		// use to index into array; then increment N
		s[N++] = item;
	}

	public Item pop() {
		// decrement N; then use to index into array
		return s[--N];
	}

}
