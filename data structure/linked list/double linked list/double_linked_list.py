"""
双向链表

"""


class Node(object):
	"""双链表 的 节点"""
	def __init__(self, item):
		self.elem = item
		self.prev = None
		self.next = None


class DoubleLinkedList(object):
	"""双链表"""

	def __init__(self, node=None):
		"""初始化"""
		self.__head = node

	def is_empty(self):
		"""判断链表是否为空。  与单链表的一样。"""
		return self.__head is None

	def length(self):
		"""获取链表长度。 与单链表的一样。"""

		# cur游标，用来移动遍历元素
		cur = self.__head
		# count，记录数量
		count = 0

		while cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
			count = count + 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表。 与单链表的一样，从前往后。"""

		cur = self.__head

		while cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
			print(cur.elem, end=" ")
			cur = cur.next
		print()

	def add(self, elem):
		"""在单链表的头部添加元素。头插法。"""
		node = Node(elem)
		node.next = self.__head
		self.__head = node

		node.next.prev = node  #

	def append(self, elem):
		"""在单链表的尾部添加元素。尾插法。"""

		node = Node(elem)

		if self.is_empty():  # 特殊情况
			self.__head = node
		else:
			cur = self.__head

			while cur.next is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
				cur = cur.next
			cur.next = node

			node.prev = cur  #

	def insert(self, pos, elem):
		"""在单链表的指定位置添加元素。

		:param pos: pos 从0开始
		"""
		if pos <= 0:  # 特殊情况
			self.add(elem)
		elif pos > (self.length() - 1):  # 特殊情况
			self.append(elem)
		else:
			cur = self.__head  # 游标
			count = 0

			while count < pos:  # Thinking：
				count += 1
				cur = cur.next

			# 当循环退出后， cur 指向 pos 的位置
			node = Node(elem)

			node.next = cur
			node.prev = cur.prev
			cur.prev.next = node
			cur.prev = node

	def remove(self, elem):
		"""删除单链表中的一个数据。 obj.remove(200) 删除掉第一个200这个数据"""

		cur = self.__head  # 游标 __cur

		while cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
			if cur.elem == elem:  # 删除条件
				# 先判断此节点是否是头节点
				# 头节点
				if cur == self.__head:
					self.__head = cur.next
					if cur.next is not None:  # if cur.next:
						# 判断链表是否只有一个节点
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev

				break
			else:
				cur = cur.next

	def search(self, elem):
		"""查找单链表中某节点元素是否存在。 与单链表一样。"""

		cur = self.__head  # 游标

		while cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?

			if cur.elem == elem:
				return True
			else:
				cur = cur.next

		return False



if __name__ == '__main__':
	# 测试节点
	node = Node(100)
	print(node, node.elem, node.next, node.prev)

	# 测试单链表
	single_obj = DoubleLinkedList()

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

	"""测试的结果，与单链表的一样：
	
	<__main__.Node object at 0x0000019D610F3DA0> 100 None None
	0
	True
	False
	7
	333 3 66 2 2 1 200 300 400 555 
	True
	333 3 66 2 1 200 300 400 555
	"""
