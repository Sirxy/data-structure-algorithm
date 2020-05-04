
class Node(object):
	"""节点"""

	def __init__(self, item, lchild=None, rchild=None):
		self.item = item  # 数据
		self.lchild = lchild  # 左孩子
		self.rchild = rchild  # 右孩子


class Tree(object):
	"""二叉树"""

	def __init__(self, root=None):
		self.root = root

	def add(self, item):
		"""为树添加节点"""

		node = Node(item)

		# 如果树是空的，则对根节点赋值
		if self.root is None:
			self.root = node
		else:
			queue = [self.root]

			# 对已有的节点进行 层次遍历
			while queue:

				cur_node = queue.pop(0)  # 弹出队列的第一个元素

				if cur_node.lchild is None:
					cur_node.lchild = node
					return
				else:
					queue.append(cur_node.lchild)

				if cur_node.rchild is None:
					cur_node.rchild = node
					return
				else:  # 如果左右子树都不为空，加入队列继续判断
					queue.append(cur_node.rchild)

	def breadth_travel(self):
		"""利用队列实现树的层次遍历 (广度优先遍历),从树的root开始，从上到下, 从左到右遍历整个树的节点"""
		if self.root is None:
			return

		queue = [self.root]

		while queue:
			cur_node = queue.pop(0)
			print(cur_node.item)

			if cur_node.lchild is not None:
				queue.append(cur_node.lchild)

			if cur_node.rchild is not None:
				queue.append(cur_node.rchild)

	def preorder(self, node):
		"""递归实现先序遍历"""
		if node == None:
			return

		print(node.item, end=' ')
		self.preorder(node.lchild)
		self.preorder(node.rchild)

	def inorder(self, node):
		"""递归实现中序遍历"""
		if node == None:
			return

		self.inorder(node.lchild)
		print(node.item, end=' ')
		self.inorder(node.rchild)

	def postorder(self, node):
		"""递归实现后续遍历"""
		if node == None:
			return

		self.postorder(node.lchild)
		self.postorder(node.rchild)
		print(node.item, end=' ')


if __name__ == '__main__':

	tree = Tree()

	tree.add(0)
	tree.add(1)
	tree.add(2)
	tree.add(3)
	tree.add(4)
	tree.add(5)
	tree.add(6)
	tree.add(7)
	tree.add(8)
	tree.add(9)

	tree.breadth_travel()
	print()
	tree.preorder(tree.root)
	print()
	tree.inorder(tree.root)
	print()
	tree.postorder(tree.root)

	"""
	0
	1
	2
	3
	4
	5
	6
	7
	8
	9
	
	0 1 3 7 8 4 9 2 5 6 
	7 3 8 1 9 4 0 5 2 6 
	7 8 3 9 4 1 5 6 2 0 
	"""
