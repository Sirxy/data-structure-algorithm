"""

"""


class Stack(object):

	def __init__(self):
		self.__list = []

	def push(self, item):
		""""""
		self.__list.append(item)
		# self.__list.insert(0, item)

	def pop(self):
		""""""
		return self.__list.pop()
		# self.__list.pop(0)

	def peek(self):
		""""""
		if self.__list:
			return self.__list[-1]
		else:
			return None

	def is_empty(self):
		""""""
		return self.__list == []

	def size(self):
		""""""
		return len(self.__list)


if __name__ == '__main__':
	s = Stack()
	print(s.is_empty())
	print()
	s.push('you')
	s.push('love')
	s.push('i')
	print(s.peek())
	print(s.size())
	print(s.is_empty())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.size())

	"""
	True
	
	i
	3
	False
	i
	love
	you
	0
	"""
