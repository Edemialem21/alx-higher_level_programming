#include <stdio.h>
#include <stdlib.h>

struct linked
{
int data;
struct linked *next;
};
void printlists(struct linked *head)
{
    struct linked *currentNode = head;

    while (currentNode != NULL)
    {
        printf("%d ", currentNode->data);
        currentNode = currentNode->next;
    }

    printf("\n");
}

void count_of_node(struct linked *head){
    int count = 0;
    if(head == NULL){
        printf("Linked  list is empty");
    }
    struct linked *ptr = NULL;
    ptr = head;
    while(ptr != NULL){
        count++;
        ptr = ptr->next;
    }
    printf("The number of nodes in this linke list is: %d\n", count);

}



int main(void)
{
    struct linked *head = (struct linked *)malloc(sizeof(struct linked));
    head->data = 120;
    head->next = NULL;

struct linked *current = (struct linked *)malloc(sizeof(struct linked));
    current->data = 1;
    current->next = NULL;
    head->next = current;

current = (struct linked *)malloc(sizeof(struct linked));
    current->data = 10;
    current->next = NULL;
    head->next->next = current;

    current = (struct linked *)malloc(sizeof(struct linked));
    current->data = 100;
    current->next = NULL;
    head->next->next->next = current;

current = (struct linked *)malloc(sizeof(struct linked));
    current->data = 8;
    current->next = NULL;
    head->next->next->next->next= current;

current = (struct linked *)malloc(sizeof(struct linked));
    current->data = 11;
    current->next = NULL;
    head->next->next->next->next->next= current;


    printf("the newely creatrd node has %d data and %p address.\n", head->data, head->next);

    printlists(head);

    count_of_node(head);
    return 0;
}
