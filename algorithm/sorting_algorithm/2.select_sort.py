

def select_sort(alist):
	""""""
	n = len(alist)

	# 需要进行n-1次选择操作
	for j in range(0, n-1):  # j  0---n-2

		# 记录最小位置
		min_index = j

		# 从 j+1 位置到末尾选择出最小数据
		for i in range(j+1, n):  #
			if alist[min_index] > alist[i]:
				min_index = i

		# 如果选择出的数据不在正确位置，进行交换
		if j != min_index:
			alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
	arr = [3, 2, 5, 1, 7, 4]
	select_sort(arr)
	print(arr)  # [1, 2, 3, 4, 5, 7]
