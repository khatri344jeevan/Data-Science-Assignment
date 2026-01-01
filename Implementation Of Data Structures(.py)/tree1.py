from anytree import Node, RenderTree
root = Node("10")
child1 = Node("5",parent=root)
child2 = Node("20",parent=root)
child3 = Node("3",parent=child1)
child4 = Node("7",parent=child1)

for pre, fill, node in RenderTree(root):
    print(pre, node.name)