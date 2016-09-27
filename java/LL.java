public class LL<T> {
  public class Node<T> {
    private T value;
    private Node<T> next;

    public Node(T v, Node<T> n) {
      this.value = v;
      this.next = n;
    }

    public Node(T v) {
      this(v, null);
    }

    public Node() {
      this(null, null);
    }

    public void setValue(T v) {
      this.value = v;
    }

    public T getValue() {
      return this.value;
    }

    public void setNext(Node<T> n) {
      this.next = n;
    }

    public Node<T> getNext() {
      return this.next;
    }

    public String toString() {
      return "value: " + this.value + " , next: " + this.next;
    }
  }

  Node<T> head, tail;
  int size;

  public LL() {
    this.head = new Node<T>();
    this.tail = this.head;
    this.size = 0;
  }

  public int getSize() {
    return this.size;
  }

  public boolean isEmpty() {
    return this.getSize() == 0;
  }

  public void push_front(T v) {
    this.head.setNext(new Node<T>(v, this.head.getNext()));
    this.size++;
    if (this.head == this.tail) {
      this.tail = this.head.getNext();
    }
  }

  public T pop_front() {
    if (this.isEmpty()) {
      throw new LLException("Empty list");
    }
    T retval = this.head.getNext().getValue();
    this.head.setNext(this.head.getNext().getNext());
    if (this.head.getNext() == null) {
      this.tail = this.head;
    }
    this.size--;
    return retval;
  }

  public void push_back(T v) {
    this.tail.setNext(new Node<T>(v));
    this.size++;
    this.tail = this.tail.getNext();
  }

  public String toString() {
    String retval = "";
    if (this.isEmpty()) {
      retval = "List is empty";
    } else {
      Node<T> p = this.head.getNext();
      while (p != null) {
        retval += p.getValue() + " --- ";
        p = p.getNext();
      }
    }
    return retval;
  }

  public static void main(String args[]) {
    LL<String> ll = new LL<String>();
    ll.push_back("Ruby");
    ll.push_front("NodeJS");
    ll.push_front("JavaScript");
    ll.push_back("Python");
    ll.push_back("C++");
    ll.push_back("C");
    ll.pop_front();

    System.out.println(ll);
    System.out.println(ll.head);
    System.out.println(ll.tail);
    System.out.println(ll.getSize());
  }
}