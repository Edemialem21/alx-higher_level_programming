void add_to_end(struce linked *head, int data)
{
    struct linked *ptr, *temp;
    temp = (struct linked*)malloc(sizeof(struct linked));
    temp->data = data;
    temp->next = NULL;
while(ptr->next != NULL)
{
    ptr = ptr->next
}
ptr->next = temp;
}