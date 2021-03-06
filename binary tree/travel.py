from Node import Node
# using recursion
def f(node):
    if not node:
        return
    # 1 pre order
    print('first',node.val)
    f(node.left)
    # 2 in order
    print('second',node.val)
    f(node.right)
    # 3 post order
    print('third',node.val)

head = Node(1)
head.left = Node(2)
head.right = Node(3)
# 该方程展示的是递归顺序，三种顺序是对递归序的不同加工
# 先序是第一次到一个节点，就打印，中序是第二次，后序是最后一次
f(head)
'''
pre order
1. stack 弹出当前cur，打印
2. 先加右再加左 (弹出顺序就是先左再右)
3. stack空停止

in order
用 stack 进行 dfs

post order
利用stack
进入顺序改为先加左再加右，这样弹出顺序则为中右左
不着急打印，收起来所有的弹出数值，逆序打印，则为左右中
'''
def inorder(head):
     if head:
         stack = []
         cur = head
         while stack or cur:
             # 阶段一 一直加左边的东西 直到没有左子树
             if cur:
                 stack.append(cur)
                 cur = cur.left
             else:
                 cur = stack.pop()
                 print(cur.val)
                 cur = cur.right

class Solution:
    def threeOrders(self , root ):
        stack = []
        ans = [[],[],[]]
        head = root
        # pre order
        stack.append(head)
        while stack:
            cur = stack.pop()
            ans[0].append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        # in order
        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans[1].append(cur.val)
                cur = cur.right
        # post order
        stack = []
        temp = []
        head = root
        stack.append(head)
        while stack:
            cur = stack.pop()
            temp.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        ans[2] = list(reversed(temp))
        return ans
