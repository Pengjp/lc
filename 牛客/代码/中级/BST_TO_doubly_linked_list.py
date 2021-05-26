class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.data)

''' Construct the following tree
          10
        /   \
       /     \
      8       12
     / \     / \
    6   9   11   13
'''

root = Node(10)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(6)
root.left.right = Node(9)
root.right.left = Node(11)
root.right.right = Node(13)

# 每个节点返回头和尾节点
class Info():
    def __init__(self,s,e):
        self.s = s
        self.e = e
    def __repr__(self):
        return f'开始{self.s} 结尾{self.e}'

def process(x):
    if not x:
        return Info(None, None)
    left = process(x.left)
    right = process(x.right)
    # 左 -> X -> 右
    # 左end -> X, X左 -> 左end
    # X右 -> 右start
    # 右start -> x右
    # 左边尾巴的left 连接到x
    if left.e:
        left.e.right = x
    x.left = left.e
    x.right = right.s
    if right.s:
        right.s.left = x

    # 返回整个树的头和尾
    return Info(left.s if left.s else x, right.e if right.e else x)

print(process(root))
