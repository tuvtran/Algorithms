/*
  Find the kth smallest item
*/
import java.util.*;

public class Quickselect {
  private static int partition(Comparable[] a, int lo, int hi) {
    int j = lo;
    Comparable x = a[lo];

    for (int i = lo + 1; i <= hi; i++) {
      if (a[i].compareTo(x) <= 0) {
        j++;
        Comparable tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
      }
    }

    Comparable tmp = a[lo];
    a[lo] = a[j];
    a[j] = tmp;

    return j;
  }

  public static Comparable select(Comparable[] a, int k) {
    int lo = 0, hi = a.length - 1;

    while (hi > lo) {
      // Randomize
      Random rand = new Random();
      int randomIndex = (int) rand.nextInt(hi - lo + 1) + lo;

      Comparable tmp = a[lo];
      a[lo] = a[randomIndex];
      a[randomIndex] = tmp;

      int j = partition(a, lo, hi);
      if (j < k)
        lo = j + 1;
      else if (j > k)
        hi = j - 1;
      else
        return a[k];
    }

    return a[k];
  }

  public static void main(String[] args) {
    Random rnd = new Random();
    Integer[] arr = new Integer[7];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = rnd.nextInt(20);
    }

    System.out.println(Arrays.toString(arr));
    System.out.println(select(arr, 0));
  }
}