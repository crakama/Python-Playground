import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

def lOrder(self, root):
	if root in None:
		return 0
	queue = []
	queue.append(root)
	while(len(queue) > 0):
		print queue[0].data,
		node = queue.pop(0)


		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(node.right)

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)







