from linkedlist import Linkedlist

# With a buffer to lookup visited values
# Space complexity: O(n)
# Time Complexity: O(n)
def remove_duplicates(head):
	visited = set()
	n = head
	prev = head
	while n:
		if n.value in visited:
			if n.next: prev.next = n.next
		else:
			visited.add(n.value)
		prev = n
		n = n.next
	return head


l = Linkedlist()
head = l.make([1, 1, 3, 5, 17, 9, 1, 23])
print remove_duplicates(head)