public class FixedCapacityStackOfStrings {

	private String[] s;
	private int N = 0;

	public FixedCapacityStackOfStrings(int capacity) {
		s = new String[capacity];
	}

	public boolean isEmpty() {
		return N == 0;
	}

	public void push(String item) {
		// use to index into array; then increment N
		s[N++] = item;
	}

	public String pop() {
		// decrement N; then use to index into array
		return s[--N];
	}

}
