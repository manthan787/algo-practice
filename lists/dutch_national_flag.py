'''
Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example,
given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''
def partition_two_colors(arr):
	''' Partition given array containing colors 'R' and 'B'
	and partition the array such that all the 'R' colored elements
	occur before 'B' colored elements.
	'''
	low, high = 0, len(arr) - 1
	while low <= high:
		print low, high
		if arr[low] == 'R':
			low += 1
		else:
			arr[low], arr[high] = arr[high], arr[low]
			high -= 1
		print arr
	return arr

def partition(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print partition(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
print partition_two_colors(['B', 'R', 'R', 'B'])