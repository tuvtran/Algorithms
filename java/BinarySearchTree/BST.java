import java.util.*;

public class BST<Key extends Comparable<Key>, Value> {
    private class Node {
        private Key key;
        private Value val;
        private Node left, right;
        private int count;

        public Node(Key key, Value val) {
            this.key = key;
            this.val = val;
        }
    }

    // root of BST
    private Node root; 

    /**
     * key in tree => replace value
     * key node in tree => add new node
     * @param key
     * @param value
     */
    public void put(Key key, Value val) {
        root = put(root, key, val);
    }

    /**
     * @param node to start searching from 
     * @param key
     * @param value
     * @return node after inserting
     */
    private Node put(Node node, Key key, Value val) {
        if (node == null)
            return new Node(key, val);

        int cmp = key.compareTo(node.key);
        if (cmp > 0)
            node.right = put(node.right, key, val);
        else if (cmp < 0)
            node.left = put(node.left, key, val);
        else
            node.val = val;

        node.count = 1 + size(node.left) + size(node.right);

        return node;
    }

    /**
    *    @param key
    *    @return value if key matches, otherwise null
    */
    public Value get(Key key) {
        return get(root, key);
    }

    /**
     * @param node to start searching
     * @param key
     * @return value
     */
    private Value get(Node node, Key key) {
        if (node == null) {
            return null;
        }

        int cmp = key.compareTo(node.key);
        if (cmp > 0)        // search the right subtree
            return get(node.right, key);
        else if (cmp < 0)   // search the left subtree
            return get(node.left, key);
        else
            return node.val;
    }

    public void delete(Key key) {

    }

    /**
     * find the floor of a key
     * @param key
     * @return another key
     */
    public Key floor(Key key) {
        Node x = floor(root, key);
        return (x == null) ? null : x.key;
    }

    /**
     * @param node to start from
     * @param key
     * @return node of the found key
     */
    private Node floor(Node node, Key key) {
        if (node == null)
            return null;

        int cmp = key.compareTo(node.key);
        
        if (cmp == 0)
            return node;

        if (cmp < 0)
            return floor(node.left, key);

        Node right = floor(node.right, key);
        return (right == null) ? node : right;
    }

    /**
     * @return size of the tree
     */
    public int size() {
        return size(root);
    }

    /**
     * @param node
     * @return size from the current node
     */
    private int size(Node node) {
        return (node == null) ? 0 : node.count;
    }

    /**
     * @param key to find rank
     * @return rank
     */
    public int rank(Key key) {
        return rank(root, key);
    }

    /**
     * @param node to find rank from
     * @param key
     * @return rank
     */
    private int rank(Node node, Key key) {
        if (node == null)
            return 0;

        int cmp = key.compareTo(node.key);

        // search the left subtree
        // the rank is the same in the left subtree
        if (cmp < 0)
            return rank(node.left, key);
        // the rank is the current node plus the left subtree plus the right subtree
        else if (cmp > 0)
            return 1 + size(node.left) + rank(node.right, key);
        // the rank is the size of its left child
        else
            return size(node.left);
    }

    /**
     * @return a queue storing keys
     */
    public Iterable<Key> iterator() {
        ArrayList<Key> queue = new ArrayList<>();
        inorder(root, queue);
        return queue;
    }

    /**
     * helper for iterator()
     * @param current node
     * @param queue
     */
    private void inorder(Node node, ArrayList<Key> queue) {
        if (node == null)
            return;

        inorder(node.left, queue);
        queue.add(node.key);
        inorder(node.right, queue);
    }
}