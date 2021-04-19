from Node import Node

head = Node(5)
head.left = Node(3)
head.right = Node(8)
head.left.left = Node(2)
head.left.right = Node(4)
head.left.left.left = Node(1)
head.right.left = Node(7)
head.right.right = Node(10)

def LCA(root, p, q):
    if not root or root == p or root == q:
        return root
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)
    if not left:
        return right
    elif not right:
        return left
    else:
        return root
print(LCA(head, head.left.left.left, head.left.right).val)

# class Info:
#     def __init__(self, findO1, findO2,findAns):
#         self.findO1 = findO1
#         self.findO2 = findO2
#         self.findAns = findAns
#
# def process(x, o1, o2):
#     if not x:
#         return Info(False, False, None)
#     leftInfo = process(x.left, o1, o2)
#     rightInfo =  process(x.left, o1, o2)
#     if leftInfo.findAns:
#         return Info(True,True,leftInfo.findAns)
#     if rightInfo.findAns:
#         return Info(True,True,rightInfo.findAns)
#     if (leftInfo.findO1 and rightInfo.findO2) or (leftInfo.findO2 and rightInfo.findO1):
#         return Info(True,True,x)
#     findO1 = x == o1
#     findO2 = x == o2
#     if
