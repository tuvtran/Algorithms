public class Stack<T> {
  LL<T> stack;

  public Stack() {
    stack = new LL<T>();
  }

  public boolean isEmpty() {
    return stack.isEmpty();
  }

  public boolean isFull() {
    return false;
  }

  public void push(T v) {
    stack.push_front(v);
  }

  public T pop() throws LLException {
    return stack.pop_front();
  }

  public static void main(String args[]) {
    Stack<String> s = new Stack<String>();

    s.push("Google");
    s.push("Facebook");
    s.push("Amazon");
    s.push("Microsoft");
    s.push("salesforce");
    s.push("Uber");

    while(!s.isEmpty()) {
      System.out.println(s.pop());
    }
  }
}