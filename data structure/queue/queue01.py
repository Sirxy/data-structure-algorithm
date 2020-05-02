"""
队列

"""


class Queue(object):

	def __init__(self):
		self.__list = []

	def enqueue(self, item):
		self.__list.append(item)
		# self.__list.insert(0, item)

	def dequeue(self):
		self.__list.pop(0)
		# self.__list.pop()

	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)


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
