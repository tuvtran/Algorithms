public class Queue<T> {
  private LL<T> queue;

  public Queue() {
    queue = new LL<T>();
  }

  public boolean isEmpty() {
    return queue.isEmpty();
  }

  public void enqueue(T v) {
    queue.push_back(v);
  }

  public T dequeue() throws LLException {
    return queue.pop_front();
  }

  public static void main(String args[]) {
    Queue<String> q = new Queue<String>();

    q.enqueue("Subaru");
    q.enqueue("Felis");
    q.enqueue("Emilia");
    q.enqueue("Rem");
    q.enqueue("Ram");

    while (!q.isEmpty()) {
      System.out.println(q.dequeue());
    }
  }
}