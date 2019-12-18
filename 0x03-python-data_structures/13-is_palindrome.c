#include "lists.h"
/**
 * is_palindrome - Will check if the list is palindrome
 * @head: Head to the first node in the list
 * Return: 1 if it is and 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ti = *head;
	listint_t *ts = *head;
	int i = 1, j, len = 0;

	if (head == NULL || *head == NULL)
		return(0);
	while (ti)
	{
		len++;
		ti = ti->next;
	}
	ti = *head;
	while (i != len)
	{
		for (j = 1; j < len; j++)
		{
			ti = ti->next;
		}
		if (ti->n != ts->n)
			return (0);
		else
		{
			ts = ts->next;
			if (ti == ts)
				break;
			ti = *head;
			len--;
			i++;
		}
	}
	return (1);
}
