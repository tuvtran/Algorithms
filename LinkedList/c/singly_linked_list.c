#include <stdio.h>
#include <stdlib.h>

#include "linked_list.h"


int main(int argc, char **argv) {
    node_t *head;

    head = create(10, NULL);
    head = push_front(20, head);
    head = push_front(30, head);
    head = push_back(100, head);

    print_list(head);
    free_list(head);

    return EXIT_SUCCESS;
}


node_t *create(int data, node_t* next) {
    node_t *new_node;

    if ((new_node = (node_t *) malloc(sizeof(node_t))) == NULL) {
        fprintf(stderr, "error allocating memory");
        return NULL;
    }

    new_node->value = data;
    new_node->next = next;

    return new_node;
}


node_t *push_front(int data, node_t *head) {
    node_t *new_head = create(data, head);
    head = new_head;
    return head;
}


node_t* push_back(int data, node_t *head) {
    node_t *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    node_t *new_node = create(data, NULL);
    current->next = new_node;
    return head;
}


void print_list(node_t *head) {
    node_t *current = head;
    while (current != NULL) {
        printf("%d-->", current->value);
        current = current->next;
    }
    printf("\n");
    return;
}


void free_list(node_t *head) {
    node_t *tmp;

    while (head != NULL) {
        tmp = head;
        head = head->next;
        free(tmp);
    }

    return;
}