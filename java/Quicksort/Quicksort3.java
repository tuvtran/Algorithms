public class Quicksort3 {
  private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo)
      return;

    int lt = lo, gt = hi;
    Comparable v = a[lo];
    int i = lo;
    while (i <= gt) {
      int cmp = a[i].compareTo(v);

      if (cmp < 0) {
        // exchange a[lt] and a[i]
        Comparable tmp = a[lt];
        a[lt] = a[i];
        a[i] = tmp;

        lt++;
        i++;
      } else if (cmp > 0) {
        // exchange a[i] and a[gt]
        Comparable tmp = a[i];
        a[i] = a[gt];
        a[gt] = tmp;

        gt--;
      } else
        i++;
    }

    sort(a, lo, lt - 1);
    sort(a, gt + 1, hi);
  }
}
