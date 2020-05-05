

def insert_sort(alist):
	""""""
	n = len(alist)
	# 从右边的序列中取出多少个元素执行这样的过程
	for j in range(1, n):  # # 从第二个位置，即下标为1的元素开始向前插入
		# j = [1, 2, 3, n-1]
		# i 代表内层循环起始值
		i = j
		# 执行从右边的无序序列中取出第一个元素，即i 位置的元素，然后将其插入到前面的正确位置中
		while i > 0:
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i-1], alist[i]
				i -= 1
			else:
				break


def insert_sort_(alist):
	n = len(alist)
	# 从右边的序列中取出多少个元素执行这样的过程
	for j in range(1, n):

		# 执行从右边的无序序列中取出第一个元素，即i 位置的元素，然后将其插入到前面的正确位置中
		for i in range(j, 0, -1):
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i-1], alist[i]
			else:
				break


if __name__ == '__main__':
	alist = [54, 26,93, 17, 77, 31, 44, 55, 20]
	insert_sort_(alist)
	print(alist)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
