"""
队列是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，和栈一样，队列是一种操作受限制的线性表。

进行插入操作的端称为队尾，进行删除操作的端称为队头。队列中没有元素时，称为空队列。

队列的数据元素又称为队列元素。在队列中插入一个队列元素称为入队，从队列中删除一个队列元素称为出队。

因为队列只允许在一端插入，在另一端删除，所以只有最早进入队列的元素才能最先从队列中删除，故队列又称为先进先出（FIFO—first in first out）线性表。

"""


class Queue(object):
	"""将 Python 列表维护成一个队列"""

	def __init__(self):
		self.elements = []

	def enqueue(self, element):
		"""元素入队列"""
		self.elements.insert(0, element)

	def dequeue(self):
		"""元素出队列"""
		self.elements.pop()

	def is_empty(self):
		"""判断队列是否为空"""
		return self.elements == []

	def size(self):
		"""获取队列大小"""
		return len(self.elements)

	# TODO 没写支持遍历队列操作


if __name__ == '__main__':
	queue = Queue()
	queue.enqueue("i")
	queue.enqueue("love")
	print(queue.is_empty())
	queue.enqueue("you")
	print(queue.size())
	print(queue.dequeue())

	"""测试结果：
	False
	3
	None
	"""
