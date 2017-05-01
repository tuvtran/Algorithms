import java.util.*;

public class Quicksort {
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

  public static void sort(Comparable[] a) {
    sort(a, 0, a.length - 1);
  }

  private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo)
      return;

    Random rand = new Random();
    int randomIndex = (int) rand.nextInt(hi - lo + 1) + lo;

    Comparable tmp = a[lo];
    a[lo] = a[randomIndex];
    a[randomIndex] = tmp;

    int j = partition(a, lo, hi);
    sort(a, lo, j - 1);
    sort(a, j + 1, hi);
  }

  public static void main(String[] args) {
    Random rnd = new Random();
    Integer[] arr = new Integer[50];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = rnd.nextInt(500);
    }

    sort(arr);
    System.out.println(Arrays.toString(arr));
  }
}