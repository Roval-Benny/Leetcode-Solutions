#: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 

class LinkedList:
	def __init__(self,data):
		self.data = data
		self.next = None
	
	def BTtoLinkedList(self,tree):
		output = []
		depth = []
		if tree:
			depth.append(tree)
		while(depth):
			temp = []
			head = None
			tail = None
			i = 0
			while i<len(depth):
				node = depth[i]
				newNode = LinkedList(node.val)
				if node.left:
					temp.append(node.left)
				if node.right:
					temp.append(node.right)
				if head==None:
					head = newNode
					tail = newNode
				else:
					tail.next = newNode
					tail = newNode
				i+=1
			depth = temp
			output.append(head)
		return output