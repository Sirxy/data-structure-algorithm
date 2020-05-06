
def binary_search(alist, item):
	"""二分查找：递归实现"""

	n = len(alist)

	if n > 0:
		mid = n // 2

		if alist[mid] == item:
			return True
		elif alist[mid] > item:
			return binary_search(alist[:mid], item)
		else:
			return binary_search(alist[mid+1:], item)
	return False


def binary_search_2(alist, item):
	"""二分查找：非递归实现"""
	n = len(alist)

	first = 0
	last = n - 1

	while first <= last:
		mid = (first + last) // 2

		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			last = mid - 1
		else:
			first = mid + 1
	return False



if __name__ == '__main__':
	alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]

	print(binary_search(alist, 55))  # True
	print(binary_search(alist, 100))  # False

	print(binary_search_2(alist, 55))  # True
	print(binary_search_2(alist, 100))  # False

