#ifndef __LLIST_H
#define __LLIST_H

#define TRUE 1
#define FALSE 0

/**
 * A linked list node
 */
typedef struct node {
    int value;
    struct node *next;
} node_t;

// create a new ndoe
node_t *create(int, node_t *);
// add to head
node_t *push_front(int, node_t *);
// add to tail
node_t *push_back(int, node_t *);
// print a linked list
void print_list(node_t *);
// free linked list nodes
void free_list(node_t *);

#endif