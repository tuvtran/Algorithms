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

    /*
        key in tree => replace value
        key not in tree => add new node

        @param key and value
    */
    public void put(Key key, Value val) {
        root = put(root, key, val);
    }

    /*
        helper function for put
        @param node to start searching from, key, value
        @return node after searching
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

    /*
        @param key
        @return value if key matches, otherwise null
    */
    public Value get(Key key) {
        return get(root, key);
    }

    /*
        helper function for get()
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

    /*
        find the floor of a key
        @param key
        @return another key
    */
    public Key floor(Key key) {
        Node x = floor(root, key);
        return (x == null) ? null : x.key;
    }

    /*
        helper function for floor()
        @param node to start from, key
        @return node of the found key
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

    /*
        return the size of the root
        @param
        @return size
    */
    public int size() {
        return size(root);
    }

    /*
        return the size of a node
        @param node
        @return size
    */
    private int size(Node node) {
        return (node == null) ? 0 : node.count;
    }

    /*
        return the rank i.e the number of keys less than
        @param key
        @return number of keys
    */
    public int rank(Key key) {
        return rank(root, key);
    }

    /*
        helper function for rank
        @param node, key
        @return number of keys
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

    /*
        inorder traversal
        @return queue storing keys
    */
    public Iterable<Key> iterator() {
        List<Key> queue = new ArrayList<>();
        inorder(root, queue);
        return queue;
    }

    /*
        helper function for iterator
        inorder traversal of the tree
    */
    private void inorder(Node node, ArrayList<Key> queue) {
        if (node == null)
            return;

        inorder(node.left, queue);
        queue.add(node.key);
        inorder(node.right, queue);
    }
}