def merge_sort(l):
	if len(l) == 1: return l
	middle = len(l) / 2
	left = merge_sort(l[0:middle])
	right = merge_sort(l[middle:])
	return merge(left, right)

def merge(l1, l2):
	ptr1 = 0
	ptr2 = 0
	merged = []
	while ptr1 < len(l1) and ptr2 < len(l2):
		if l1[ptr1] < l2[ptr2]:
			merged.append(l1[ptr1])
			ptr1 += 1
		else:
			merged.append(l2[ptr2])
			ptr2 += 1

	while ptr1 < len(l1):
		merged.append(l1[ptr1])
		ptr1 += 1

	while ptr2 < len(l2):
		merged.append(l2[ptr2])
		ptr2 += 1
	return merged

print merge_sort([1, 9, 2, 7, 11, 3])
print merge_sort([1])
print merge_sort([9, 9])