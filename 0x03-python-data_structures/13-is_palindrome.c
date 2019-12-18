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
	char array[9999];
	int i = 1, j, len = 0;

	if (*head == NULL)
		return (1);
	len = list_len(ti);
	for (i = 0; i < len; i++)
	{
		array[i] = ti->n;
		ti = ti->next;
	}
	i = 0;
	for (i = 0, j = len - 1; i < len; i++, j--)
	{
		if (array[i] != array[j])
		{
			return (0);
		}
	}
	return (1);
}
