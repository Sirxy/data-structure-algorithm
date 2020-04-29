"""
选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

动图演示
见images/selection_sort.gif

算法步骤
1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3.重复第二步，直到所有元素均排序完毕。
"""


def selection_sort(arr):
	for i in range(len(arr) - 1):
		# 记录最小数的索引
		min_index = i

		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		# i 不是最小数时，将 i 和最小数进行交换
		if i != min_index:
			arr[i], arr[min_index] = arr[min_index], arr[i]

	return arr


if __name__ == '__main__':
	arr = [3, 2, 5, 1, 7, 4]
	selection_sort(arr)
	print(arr)  # [1, 2, 3, 4, 5, 7]

