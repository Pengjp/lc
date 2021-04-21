''' with a parent node '''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent  = None

def inorderSuccessor(root, p):
    if p.right:
        leftmost = p.right
        while leftmost.left:
            leftmost = leftmost
        return leftmost
    else:
        parent = p.parent
        while parent and parent.left != p:
            p = parent
            parent = p.parent
        return parent

''' for a BST '''
def inorderSuccessor(root, p):
    suc = None
    while root:
        if p.val >= root:
            root = root.right
        else:
            suc = root
            root = root.left
    return suc
