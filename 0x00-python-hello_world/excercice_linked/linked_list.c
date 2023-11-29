#include <stdio.h>
#include <stdlib.h>

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
/**
 * insertNode- function to insert a new node at the beginigg
 * @headRef: the referance
 * @data: the data variable for the node
 * Return: return zero
 */
void insertNode(struct Node **headRef, int data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *headRef;
    *headRef = newNode;
}

/**
 * editNode - function to edit the value of a node at a given position
 * @head: the poiinter to the head of the node
 * @newdata: the data variable for the node
 * @position: the postion to which we need to edit
 * Return: return zero
 */
void editNode(struct Node *head, int position, int newdata)
{
    struct Node *currentNode = head;
    int currentposition = 0;

    while (currentNode != NULL && currentposition < position)
    {
        currentNode = currentNode->next;
        currentposition++;
    }
    if (currentNode != NULL)
    {
        currentNode->data = newdata;
        printf("the new data is inserted at the specified posit. \n");
    }
    else
    {
        printf("position out of range. \n");
    }
}

/**
 * deleteNode - function to delete the node at a position
 * @head: the poiinter to the head of the node
 * @position: the postion to which we need to edit
 * Return: return zero
 */
void deleteNode(struct Node **head, int position)
{
    if (*head == NULL)
    {
        printf("Lis is empty. \n");
        return;
    }
    struct Node *currentNode = *head;
    int current = 0;
    if (position == 0)
    {
        *head = currentNode->next;
        free(currentNode);
        return;
    }
    struct Node *prevnode = NULL;
    current = 0;
    while (currentNode != NULL && current < position)
    {
        prevnode = currentNode;
        currentNode = currentNode->next;
        current++;
    }

    if (currentNode == NULL)
    {
        printf("position out of range. \n");
        return;
    }
    prevnode->next = currentNode->next;
    free(currentNode);
}

/**
 * printlists - function to print linked lists
 * @head: the poiinter to the head of the node
 * Return: return zero
 */
void printlists(struct Node *head)
{
    struct Node *currentNode = head;

    while (currentNode != NULL)
    {
        printf("%d ", currentNode->data);
        currentNode = currentNode->next;
    }

    printf("\n");
}

/**
 * main - the main funcu=tion entry point
 * Return: return 0 with success
 */
int main(void)
{
    struct Node *head = NULL;
    insertNode(&head, 3);
    insertNode(&head, 7);
    insertNode(&head, 9);
    insertNode(&head, 5);
    printf("Initial linked list: ");
    printlists(head);

    editNode(head, 2, 1);
    printf("Linked list after editing at position 2: ");
    printlists(head);

    deleteNode(&head, 1);
    printf("Linked list after deleting node at position 1: ");
    printlists(head);

    return (0);
}