

def select_sort(alist):
	""""""
	n = len(alist)

	for j in range(0, n-1):  # j  0---n-2

		min_index = j

		for i in range(j+1, n):  #
			if alist[min_index] > alist[i]:
				min_index = i

		# if j != min_index:
		alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
	arr = [3, 2, 5, 1, 7, 4]
	select_sort(arr)
	print(arr)  # [1, 2, 3, 4, 5, 7]
