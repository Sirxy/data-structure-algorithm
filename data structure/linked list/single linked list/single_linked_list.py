"""
单链表


"""


class Node(object):
	"""定义一个节点类：包含一个存储元素区域和一个指向下个节点的位置"""

	def __init__(self, element):
		self.element = element
		self.next = None


class SingleLinkList(object):
	"""单链表：__head...节点1..节点2...None """

	def __init__(self, node=None):
		"""单链表初始化时，它的头 指向一空节点"""

		self.__head = node

	def is_empty(self):
		"""判断单链表是否为空。"""
		# return True if self.__head is None else False
		return self.__head is None

	def length(self):
		"""获取单链表长度。"""

		# cur游标，用来移动遍历元素
		__cur = self.__head
		# count，记录数量
		count = 0

		while __cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
			count = count + 1
			__cur = __cur.next
		return count

	def travel(self):
		"""遍历整个单链表。"""

		__cur = self.__head

		while __cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
			print(__cur.element, end=" ")
			__cur = __cur.next
		print()

	def add(self, elem):
		"""在单链表的头部添加元素。头插法。"""
		node = Node(elem)
		node.next = self.__head
		self.__head = node

	def append(self, elem):
		"""在单链表的尾部添加元素。尾插法。"""

		node = Node(elem)

		if self.is_empty():  # 特殊情况
			self.__head = node
		else:
			__cur = self.__head

			while __cur.next is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
				__cur = __cur.next
			__cur.next = node

	def insert(self, pos, elem):
		"""在单链表的指定位置添加元素。

		:param pos: pos 从0开始
		"""
		if pos <= 0:  # 特殊情况
			self.add(elem)
		elif pos > (self.length() - 1):  # 特殊情况
			self.append(elem)
		else:
			__pre = self.__head  # 游标
			count = 0

			while count < (pos - 1):  # Thinking：
				count += 1
				__pre = __pre.next

			# 当循环退出后，__pre指向 pos - 1 的位置
			node = Node(elem)
			node.next = __pre.next
			__pre.next = node

	def remove(self, elem):
		"""删除单链表中的一个数据。 obj.remove(200) 删除掉第一个200这个数据"""

		__cur = self.__head  # 游标 __cur
		__pre = None  # 游标 __pre

		while __cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
			if __cur.element == elem:  # 删除条件
				# 先判断此节点是否是头节点
				# 头节点
				if __cur == self.__head:
					self.__head = __cur.next
				else:
					__pre.next = __cur.next  # __pre.next = __pre.next.next
				break
			else:
				# 先移动__pre： __pre = __cur, __cur = __cur.next
				__pre = __cur
				__cur = __cur.next

	def search(self, element):
		"""查找单链表中某节点元素是否存在。"""

		__cur = self.__head  # 游标

		while __cur is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?

			if __cur.element == element:
				return True
			else:
				__cur = __cur.next

		return False


if __name__ == '__main__':
	# 测试节点
	node = Node(100)
	print(node, node.element, node.next)

	# 测试单链表
	single_obj = SingleLinkList()

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
	<__main__.Node object at 0x0000024FC3E212B0> 100 None
	0
	True
	False
	7
	333 3 66 2 2 1 200 300 400 555 
	True
	333 3 66 2 1 200 300 400 555 
	"""
