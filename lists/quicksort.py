'''
A quick sort implementation
'''
def quicksort(a):
	def sort(a, start, end):
		if start < end:
			part = partition(a, start, end)
			sort(a, start, part - 1)
			sort(a, part + 1, end)
	sort(a, 0, len(a) - 1)
	print a

def partition(a, start, end):
	'''
		Partition the given array `a` such that, all the values less than
		some pivot element is on the left side (in any order) and all the
		values greater than the pivot element are on the right side.

		Pivot element can be chosen either as the first element in the list
		or the last or a random element.

		-- First and last element as pivot results in O(n^2) complexity if the
		list is already sorted.
		-- Choosing random pivot reduces the probability of that happening and is
		O(n log n) in practice.
	'''
	if len(a) == 1: return start
	pivot = start
	left = start + 1
	right = end
	done = False

	while not done:

		while left <= right and a[left] <= a[pivot]:
			left += 1

		while right >= left and a[right] >= a[pivot]:
			right -= 1

		if right < left:
			done = True
		else:
			a[left], a[right] = a[right], a[left]

	a[right], a[pivot] = a[pivot], a[right]
	return right

def test_partition(l):
	print partition(l, 0, len(l) - 1)

# def test_quicksort(l):
# 	print quicksort(l, 0, len(l) - 1)

l = [7, 3, 9, 10, 2, 1]
l1 = [10, 9]
l2 = [2]
test_partition(l)
test_partition(l1)
test_partition(l2)
quicksort([54,26,93,17,77,31,44,55,20])
quicksort(l)