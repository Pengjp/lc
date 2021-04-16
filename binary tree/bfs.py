from collections import deque
from Node import Node
# BFS
'''
            1
         2     3
      4    5   6  7
'''
head = Node(1)
head.left = Node(2)
head.right = Node(3)
head.left.left = Node(4)
head.left.right = Node(5)
head.right.left = Node(6)
head.right.right = Node(7)

def bfs(head):
    queue = deque()
    queue.append(head)
    while queue:
        cur = queue.popleft()
        print(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
# bfs(head)

''' 判断树的最大宽度 '''
head = Node(1)
head.left = Node(2)
head.right = Node(3)
head.left.left = Node(4)
head.left.right = Node(5)
head.right.left = Node(6)
head.right.right = Node(7)
head.left.right.right = Node(8)
head.right.left.left = Node(9)
head.right.right.right = Node(10)

def max_width(head):
    levelMap = {} # record level for each node
    queue = deque()
    queue.append(head)
    levelMap[head] = 1
    curLevel = 1 # current level
    cnt_node = 0 # record number of nodes for each level
    max_cnt = 0 # record answer
    while queue:
        cur = queue.popleft()
        level = levelMap[cur]

        if level == curLevel: # if current node is same level, add node counts
            cnt_node += 1
        else: # if we go one level down
            print('level',curLevel,'nodes',cnt_node)
            max_cnt = max(max_cnt, cnt_node)
            curLevel += 1
            cnt_node = 1

        print('Node',cur.val,'level',levelMap[cur])

        if cur.left:
            queue.append(cur.left)
            levelMap[cur.left] = level+1
        if cur.right:
            queue.append(cur.right)
            levelMap[cur.right] = level+1

    return max(max_cnt, cnt_node) # we neeed to check the last level
print('max width is', max_width(head))
