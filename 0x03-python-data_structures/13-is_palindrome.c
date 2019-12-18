#include "lists.h"
/**
 * list_len - Will check the list of the len
 * @head: Head to the first node:
 * Return: the lenght
 */
int list_len(listint_t *head)
{	int len = 0;

	while (head)
	{
		len++;
		head = head->next;
	}
	return (len);
}
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

	if (*head == NULL)
		return (1);
	len = list_len(ti);
	ti = *head;
	while (i != len)
	{
		for (j = 1; j < len; j++)
		{
			ti = ti->next;
		}
		if (ti->n != ts->n)
		{
			return (0);
		}
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
