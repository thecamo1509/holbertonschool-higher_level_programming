#include "lists.h"
/**
* check_cycle - This function will check if a list has a cycle
* @list: The list to check
* Return: This will return 0 if the list has no cycle or 1 if it has
*/
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list->next;

	while (1)
	{
		if (!temp2 || !temp2->next)
		return (0);

		else if (temp2 == temp || temp2->next == temp)
		return (1);

		else
		{
			temp = temp->next;
			temp2 = temp2->next->next;
		}
	}
	return (0);
}
