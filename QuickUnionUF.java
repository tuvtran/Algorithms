public class QuickUnionUF {
	
	private int[] id;

	public QuickUnionUF(int n) {
		id = new int[n];
		for(int i = 0; i < n; i++) {
			id[i] = i;
		}
	}

	private int root(int i) {
		while(i != id[i]) {
			i = id[i];
		}

		return i;
	}

	public boolean connected(int p, int q) {
		return root(p) == root(q);
	}

	public void union(int p, int q) {
		int i = root(p);
		int j = root(q);

		id[i] = j;
	}

	public String toString() {
		String retval = ""; 

		for(int i = 0; i < id.length; i++) {
			retval += id[i] + " ";
		}

		return retval;
	}


	public static void main(String args[]) {
		QuickUnionUF arr = new QuickUnionUF(10);

		arr.union(0, 8);
		arr.union(7, 8);
		arr.union(4, 3);
		arr.union(1, 2);
		arr.union(7, 3);
		arr.union(5, 6);
		arr.union(1, 5);
		arr.union(6, 3);
		arr.union(5, 9);
		System.out.println(arr);

	}

}
