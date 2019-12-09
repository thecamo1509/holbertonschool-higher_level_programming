#include "lists.h"
/**
* check_cycle - This function will check if a list has a cycle
* @list: The list to check
* Return: This will return 0 if the list has no cycle or 1 if it has
*/
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	while (temp && temp->next)
	{
		temp = temp->next;
		if (temp == list)
		return(1);
	}
	return(0);
}
