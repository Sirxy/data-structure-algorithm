

def bubble_sort(alist):
	""""""
	n = len(alist)
	for j in range(0, n-1):  # 班长从头走到尾, 班长重复多少次数,外层循环控制走(比较)多少次

		count = 0  # 加入count进行优化，但最优时间复杂度没有变化

		for i in range(0, n-1-j):  # 班长从头走到尾, 内层循环控制从头走到尾

			if alist[i] > alist[i + 1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				count += 1

		if count == 0:
			return


def bubble_sort_(alist):
	for j in range(len(alist)-1, 0, -1):
		# j表示每次遍历需要比较的次数，是逐渐减小的
		for i in range(j):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
	alist = [3, 2, 5, 1, 7, 4]
	# bubble_sort(alist)
	bubble_sort_(alist)
	print(alist)  # [1, 2, 3, 4, 5, 7]
