class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root=TreeNode('R')
A=TreeNode('A')
B=TreeNode('B')
C=TreeNode('C')
D=TreeNode('D')
E=TreeNode('E')
F=TreeNode('F')
G=TreeNode('G')

root.left=A
root.right=B
A.left=C
A.right=D
B.left=E
B.right=F
F.left=G

def inOrder(node):
    if not node:
        return
    inOrder(node.left)
    print(node.data)
    inOrder(node.right)

inOrder(root)