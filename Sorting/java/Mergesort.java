import java.util.*;

public class Mergesort {
  public static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi) {
    for (int i = lo; i <= hi; i++)
      aux[i] = a[i];

    int i = lo, j = mid + 1;
    for (int k = lo; k <= hi; k++) {
      if (i > mid)
        a[k] = aux[j++];
      else if (j > hi)
        a[k] = aux[i++];
      else if (aux[i].compareTo(aux[j]) <= 0)
        a[k] = aux[i++];
      else
        a[k] = aux[j++];
    }
  }

  public static void sort(Comparable[] a, Comparable[] aux, int lo, int hi) {
    if (hi <= lo)
      return;

    int mid = lo + (hi - lo)/2;
    sort(a, aux, lo, mid);
    sort(a, aux, mid + 1, hi);
    merge(a, aux, lo, mid, hi);
  }

  public static void sortImproved1(Comparable[] a, Comparable[] aux, int lo, int hi) {
    /*
     * stop if already sorted
     */
    if (hi <= lo)
      return;

    int mid = lo + (hi - lo)/2;
    sort(a, aux, lo, mid);
    sort(a, aux, mid + 1, hi);
    if (a[mid + 1].compareTo(a[mid]) > 0)
      return;
    merge(a, aux, lo, mid, hi);
  }

  public static void sort(Comparable[] a) {
    Comparable[] aux = new Comparable[a.length];
    sort(a, aux, 0, a.length - 1);
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
