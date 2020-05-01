"""


"""


class Node(object):

	def __init__(self, elem):
		self.elem = elem
		self.next = None


node = Node(2)


class OneWayCircularList(object):

	def __init__(self, node=None):
		self.__head = node

		if node:  #
			node.next = node

	def is_empty(self):
		"""判断链表是否为空"""
		return self.__head is None

	def length(self):
		"""返回链表的长度"""

		if self.is_empty():  # 特殊情况
			return 0

		cur = self.__head  # 游标
		count = 1  # 记录数量
		while cur.next != self.__head:  # 退出条件
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历"""

		if self.is_empty():  # 空链表处理
			return

		cur = self.__head  # 游标
		while cur.next != self.__head:  # 退出循环条件
			print(cur.elem, end=' ')
			cur = cur.next

		# 退出循环，cur指向尾节点，但是节点的元素未打印
		print(cur.elem)

	def add(self, item):
		"""在头部添加一个节点"""

		node = Node(item)

		if self.is_empty():  # 特殊情况，一上来是一个空链表的话
			self.__head = node
			node.next = node
		else:
			# 先找到尾节点，将尾节点的指针指向新节点（所以需要遍历了）
			cur = self.__head
			while cur.next != self.__head:  # 退出条件
				cur = cur.next
			# 退出循环，cur指向尾节点

			node.next = self.__head  # 新节点的指向
			self.__head = node  # 头指向新节点
			cur.next = node  # 或者 cur.next = self.__head，完成尾节点的指向

	def append(self, item):
		"""在尾部添加一个节点"""

		node = Node(item)

		if self.is_empty():
			self.__head = node
			node.next = node

		else:
			cur = self.__head
			while cur.next != self.__head:  # 退出条件
				cur = cur.next
			#

			node.next = self.__head
			cur.next = node

	def insert(self, pos, item):
		"""在指定位置pos添加节点"""

		if pos <= 0:
			self.add(item)
		elif pos > self.length() - 1:
			self.append(item)
		else:  # 中间的位置插入
			pre = self.__head  # 游标
			count = 0

			while count < pos - 1:  # 条件
				count += 1
				pre = pre.next

			# 退出循环，pre指向pos - 1 的位置
			node = Node(item)
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		"""删除一个节点"""

		if self.is_empty():
			return

		# 两个游标
		cur = self.__head  # 游标
		pre = None  # pre 游标
		while cur.next != self.__head:
			if cur.elem == item:
				# 先判断此节点是否是头节点
				# 头节点
				if cur == self.__head:
					# 头节点的情况
					# 找尾节点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
				else:
					# 中间节点
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next

		# 退出循环，cur指向的是尾节点
		if cur.elem == item:
			if cur == self.__head:
				# 链表只有一个节点
				self.__head = None
			else:
				pre.next = cur.next

	def search(self, item):
		"""查找节点是否存在"""

		if self.is_empty():
			return False

		cur = self.__head
		while cur.next != self.__head:  # 退出循环条件
			if cur.elem == item:
				return True
			else:
				cur = cur.next

		# 退出循环指向尾节点
		if cur.elem == item:
			return True

		return False


if __name__ == '__main__':
	# 测试节点
	node = Node(100)
	print(node, node.elem, node.next)

	# 测试单链表
	single_obj = OneWayCircularList()

	print(single_obj.length())  #
	print(single_obj.is_empty())  #

	single_obj.append(200)  # 尾插法
	single_obj.append(300)
	single_obj.append(400)

	single_obj.add(1)  # 头插法
	single_obj.add(2)
	single_obj.add(2)
	single_obj.add(3)

	print(single_obj.is_empty())
	print(single_obj.length())

	single_obj.insert(-2, 333)
	single_obj.insert(2, 66)
	single_obj.insert(12, 555)

	single_obj.travel()

	print(single_obj.search(3))

	single_obj.remove(2)
	single_obj.travel()

	"""测试结果：
	<__main__.Node object at 0x00000238AF842358> 100 None
	0
	True
	False
	7
	333 3 66 2 2 1 200 300 400 555
	True
	333 3 66 2 1 200 300 400 555
	"""







