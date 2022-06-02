#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: points to the beginning of the list
 * @number: number to be inserted
 * Return: address to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_node;

	current_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*current_node == NULL || current_node->n >= number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
			
	while (current_node && current_node->next && current_node->next->n < number)
		{
			current_node = current_node->next;
		}
		new_node->next = current_node->next;
		current_node->next = new_node;
	}
	return (new_node);
}
