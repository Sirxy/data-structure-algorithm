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

	def add(self, item):
		"""在单链表的头部添加元素。头插法。"""
		node = Node(item)
		node.next = self.__head
		self.__head = node

	def append(self, item):
		"""在单链表的尾部添加元素。尾插法。"""

		node = Node(item)

		if self.is_empty():  # 特殊情况
			self.__head = node
		else:
			__cur = self.__head

			while __cur.next is not None:  # Thinking:循环的结束条件是 __cur.next is not None 还是 __cur is not None?
				__cur = __cur.next
			__cur.next = node

	def insert(self, pos, item):
		"""在单链表的指定位置添加元素。

		:param pos: pos 从0开始
		"""
		if pos <= 0:  # 特殊情况
			self.add(item)
		elif pos > (self.length() - 1):  # 特殊情况
			self.append(item)
		else:
			__pre = self.__head  # Thinking：
			count = 0

			while count < (pos - 1):  # Thinking：
				count += 1
				__pre = __pre.next

			# 当循环退出后，__pre指向 pos - 1 的位置
			node = Node(item)
			node.next = __pre.next
			__pre.next = node

	def remove(self, item):
		"""删除单链表中的一个元素节点。"""

	def search(self, item):
		"""查找单链表中某节点元素是否存在。"""


if __name__ == '__main__':

	# node = Node(100)
	# print(node, node.element, node.next)

	single_obj = SingleLinkList()
	print(single_obj.length())  #
	print(single_obj.is_empty())  #

	single_obj.append(200)  # 尾插法
	single_obj.append(300)
	single_obj.append(400)

	single_obj.add(1)  # 头插法
	single_obj.add(2)
	single_obj.add(3)

	print(single_obj.is_empty())
	print(single_obj.length())

	single_obj.insert(-2, 333)
	single_obj.insert(2, 66)
	single_obj.insert(12, 555)

	single_obj.travel()
