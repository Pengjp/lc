''' 判断是否为 binary search tree (bst)
'''
# 可以用 in order traversal
''' 判断 一个树为 binary search tree（head node is x） 的条件
    1. x 的左右子树整体分别为bst
    2. 左数的最大值小于x，右数的最小值大于x

    构建函数：
    对于任何一个节点而言，我需要知道三件事情
    1. 是否为bst bool
    2. 该树上的最大值 用来判断左子树
    3. 该树上的最小值 用来判断右子树
'''

class Info:
    def __init__(self, isBST, mi, ma):
        self.isBST = isBST
        self.minval = mi
        self.maxval = ma

from Node import Node

def process(x: Node)-> Info:
    if not x:
        return None
    # get information from both left and right subtrees
    leftData = process(x.left)
    rightData = process(x.right)
    # the max and min for a single node is itself if it doesn't have any subtrees
    minval = x.val
    maxval = x.val
    # if current node has subtrees, compare min and max to its subtrees
    if leftData:
        minval = min(minval, leftData.minval)
        maxval = max(maxval, leftData.maxval)
    if rightData:
        minval = min(minval, rightData.minval)
        maxval = max(maxval, rightData.maxval)
    isBst = False
    leftflag = False
    rightflag = False
    if not leftData or (leftData and (leftData.maxval < x.val and leftData.isBST)):
        leftflag = True
    if not rightData or (rightData and (rightData.minval > x.val and rightData.isBST)):
        rightflag = True
    if leftflag and rightflag:
        isBst = True
    return Info(isBst, minval, maxval)

head = Node(5)
head.left = Node(3)
head.right = Node(8)
head.left.left = Node(2)
head.left.right = Node(4)
head.left.left.left = Node(1)
head.right.left = Node(7)
head.right.right = Node(10)

ans = process(head)
print(ans.isBST,ans.minval,ans.maxval)
