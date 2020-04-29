"""
栈（stack）又名堆栈，它是一种运算受限的线性表。

限定仅在表尾进行插入和删除操作的线性表。这一端被称为栈顶，相对地，把另一端称为栈底。

向一个栈插入新元素又称作进栈、入栈或压栈，它是把新元素放到栈顶元素的上面，使之成为新的栈顶元素；

从一个栈删除元素又称作出栈或退栈，它是把栈顶元素删除掉，使其相邻的元素成为新的栈顶元素。

"栈“者，存储货物或供旅客住宿的地方,可引申为仓库、中转站，所以引入到计算机领域里，就是指数据暂时存储的地方，所以才有进栈、出栈的说法。

—— https://baike.baidu.com/item/%E6%A0%88/12808149?fr=aladdin

"""


class Stack(object):
	"""将 Python list列表 维护成一个栈"""

	def __init__(self):
		self.elements = []

	def push(self, element):
		"""添加一个新元素element到栈顶"""
		self.elements.append(element)

	def pop(self):
		"""弹出栈顶元素"""
		if self.is_empty():
			return 'stack  is empty.'
		return self.elements.pop()

	def is_empty(self):
		"""判断栈是否为空栈"""
		return self.elements == []

	def top(self):
		"""返回栈顶元素"""
		return self.elements[len(self.elements) - 1]

	def size(self):
		"""返回栈的元素个数"""
		return len(self.elements)


if __name__ == '__main__':
	stack = Stack()
	print(stack.is_empty())
	print()
	stack.push('you')
	stack.push('love')
	stack.push('i')
	print(stack.top())
	print(stack.size())
	print(stack.is_empty())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.size())

	"""测试结果：
	True
	
	i
	3
	False
	i
	love
	you
	0
	"""
