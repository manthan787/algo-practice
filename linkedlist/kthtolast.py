from linkedlist import Linkedlist

def kth_to_last(head, k):
	n = head
	runner = head
	tmp = head
	for i in xrange(k):
		runner = tmp.next
		tmp = tmp.next
	while runner:
		n = n.next
		runner = runner.next
	return n

l = Linkedlist()
head = l.make([1, 1, 3, 5, 17, 9, 1, 23])
print kth_to_last(head, 5).value