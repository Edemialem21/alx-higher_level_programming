#ifndef LINKED_H
#define LINKED_H

/**
 * struct Node - structure for a node in the linked list
 * @data: the data for a node
 * @next: the pointer tho the next node
 */

struct Node
{
    int data;
	struct Node *next;
};


#endif