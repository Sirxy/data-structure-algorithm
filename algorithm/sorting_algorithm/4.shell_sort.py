

def shell_sort(alist):
	""""""
	# n = 9
	n = len(alist)
	# gap = 4

	# 初始步长
	gap = n // 2

	# i = gap
	# for i in range(gap, n):
	# 	i = [gap, gap+1, gap+2, gap+3,... ,n-1]
	# 	while :
	# 		if alist[i] < alist[i - gap]:
	# 			alist[i], alist[i - gap] = alist[i - gap], alist[i]

	# gap 变化到0之前，插入算法执行的次数
	while gap > 0:

		# 插入算法，与普通的插入算法的区别就是gap步长
		# 按步长进行插入排序
		for j in range(gap, n):
			# j = [gap, gap + 1, gap + 2, gap + 3, ..., n - 1]
			# i 代表内层循环起始值
			i = j
			# 插入排序
			while i > 0:
				if alist[i] < alist[i - gap]:
					alist[i], alist[i - gap] = alist[i - gap], alist[i]
					i -= gap
				else:
					break
		# 缩短gap步长，得到新的步长
		gap //= 2


if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	shell_sort(alist)
	print(alist)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
