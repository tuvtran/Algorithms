import java.lang.Comparable;
import java.util.Random;
import java.util.Arrays;

public class Heapsort {
  public static void sort(Comparable[] a) {
    int N = a.length;

    // heapify the array
    for (int k = N/2; k >= 1; k--)
      sink(a, k, N);

    while (N > 1) {
      swap(a, 1, N);
      sink(a, 1, --N);
    }
  }

  private static void sink(Comparable[] a, int k, int N) {
    while (2*k <= N) {
      int j = 2*k;
      if (j < N && less(a, j, j + 1))
        j++;    // chosse the bigger child to swap
      if (!less(a, k, j))
        break;  // if all the children are smaller
      swap(a, k, j);
      k = j;
    }  
  }

  private static boolean less(Comparable[] a, int i, int j) {
    return a[i - 1].compareTo(a[j - 1]) < 0;
  }

  private static void swap(Comparable[] a, int i, int j) {
    Comparable temp = a[i - 1];
    a[i - 1] = a[j - 1];
    a[j - 1] = temp;
  }

  public static void main(String[] args) {
    Random rand = new Random();
    Integer[] arr = new Integer[50];

    for (int i = 0; i < arr.length; i++) {
      arr[i] = rand.nextInt(500);
    }

    sort(arr);
    System.out.println(Arrays.toString(arr));
  }
}