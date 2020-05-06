
def quick_sort(alist, start, end):
	"""快速排序"""

	# n = len(alist)
	mid_value = alist[start] #  alist[0]  # 设定起始元素为要寻找位置的基准元素
	low = start  # 0  # low为序列左边的由左向右移动的游标
	high = end  #  n - 1  # high为序列右边的由右向左移动的游标

	while low < high:
		# 如果 low 与 high 未重合，high 指向的元素不比基准元素小，则  high 向左移动
		while low < high and alist[high] > mid_value:
			high -= 1
		# 将 high 指向的元素放到 low 的位置上
		alist[low] = alist[high]
		low += 1

		# 如果 low 与 high 未重合，low 指向的元素比基准元素小，则 low 向右移动
		while low < high and alist[low] < mid_value:
			low += 1
		# 将 low 指向的元素放到 high 的位置上
		alist[high] = alist[low]
		high -= 1

	# 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
	# 将基准元素放到该位置
	alist[low] = mid_value

	# 对基准元素左边的子序列进行快速排序
	quick_sort(alist, start, low - 1)

	# 对基准元素右边的子序列进行快速排序
	quick_sort(alist, low + 1, end)


if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(alist, 0, len(alist) - 1)
	print(alist)

