from Node import Node

head = Node(1)
head.left = Node(1)
head.left.right = Node(1)
''' pre order '''
def serialize(head):
    if not head:
        return '#_'
    res = str(head.val) + '_'
    res += serialize(head.left)
    res += serialize(head.right)
    return res
from collections import deque

def deserialize(preStr):
    values = preStr.split('_')
    queue = deque()
    for i in values[:-1]:
        queue.append(i)
    def rebuild(queue):
        value = queue.popleft()
        if value == '#':
            return None
        head = Node(int(value))
        head.left = rebuild(queue)
        head.right = rebuild(queue)
        return head
    return rebuild(queue)

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.right, level + 1)

tree = deserialize(serialize(head))
printTree(tree)
print('---original---')
printTree(head)
