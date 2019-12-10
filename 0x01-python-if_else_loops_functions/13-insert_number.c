#include "lists.h"
/**
* insert_node - Function that inserts node sorted
* @head:  pointer to the first node
* @number: value
* Return: The new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t **temp = head;
	listint_t *new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	while (temp)
	{
		if (temp->n > number)
		{
			new->next = head;
			head = new;
			new->n = number;
		}
		if (temp->next->n > number && temp->n < number)
		{
			new->next = temp->next;
			temp->next = new;
			new->n = number;
		}
	}
	return (*head);
}
