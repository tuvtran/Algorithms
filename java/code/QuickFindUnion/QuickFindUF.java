public class QuickFindUF {

	private int[] id;
	
	public QuickFindUF(int n) {
		id = new int[n];
		for(int i = 0; i < n; i++) {
			id[i] = i;
		}
	}

	public boolean connected(int p, int q) {
		return id[p] == id[q];
	}

	public void union(int p, int q) {
		int pid = id[p];
		int qid = id[q];

		for(int i = 0; i < id.length; i++) {
			if(id[i] == pid) {
				id[i] = qid;
			}
		}
	}

	public String toString() {
		String retval = ""; 

		for(int i = 0; i < id.length; i++) {
			retval += id[i] + " ";
		}

		return retval;
	}

	public static void main(String args[]) {
		QuickFindUF arr = new QuickFindUF(10);

		arr.union(9, 1);
		arr.union(0, 3);
		arr.union(2, 9);
		arr.union(9, 4);
		arr.union(4, 7);
		arr.union(0, 4);
		System.out.println(arr);

	}

}
