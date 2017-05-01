import java.lang.Comparable;;

public class MaxPQ<Key extends Comparable<Key>> {
  private Key[] pq;
  private int size;

  // create a priority queue
  public MaxPQ(int capacity) {
    pq = (Key[]) new Comparable[capacity + 1];
  }

  // percolate up
  private void swim(int k) {
    // if parent < child then switch
    while (k > 1 && less(k/2, k)) {
      swap(k, k/2);
      k = k/2;
    }
  }

  // percolate down
  private void sink(int k) {
    while (2*k <= size) {
      int j = 2*k;
      if (j < size && less(j, j + 1))
        j++;    // chosse the bigger child to swap
      if (!less(k, j))
        break;  // if all the children are smaller
      swap(k, j);
      k = j;
    }
  }

  // insert key into the priority queue
  public void insert(Key key) {
    pq[++size] = key;
    swim(size);
  }

  // delete the max item from the queue and return it 
  public Key delMax() {
    Key max = pq[1];
    swap(1, size--);
    sink(1);
    pq[size + 1] = null;      // avoid loitering

    return max;
  }

  // check if the queue is empty
  public boolean isEmpty() {
    return size == 0;
  }

  // return the max item in the queue without deleting it 
  public Key max() {
    return pq[1];
  }

  // return the current size of the queue
  public int size() {
    return size;
  }

  // array helper method
  private boolean less(int i, int j) {
    return pq[i].compareTo(pq[j]) < 0;
  }

  private void swap(int i, int j) {
    Key t = pq[i];
    pq[i] = pq[j];
    pq[j] = pq[i];
  }
}