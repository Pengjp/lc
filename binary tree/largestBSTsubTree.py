'''
最大的BST子树需要满足的条件如下
1 如果和当前节点有关，则证明当前节点满足bst，当前节点值大于左数的最大值和小于右树的最小值
    则为左子树和右子树size的最大值
2 和当前节点无关，则当前树不是bst
    则返回左和右答案的最大值
则对于左右子树来说，我们需要三个信息，子树的最大最小值和bst的size
'''
MAX_VALUE = 99999999
MIN_VALUE = -99999999
def helper(root):
    if not root: # 如果是空节点，则bst的size是0
        return [MIN_VALUE, MAX_VALUE，0] # 当前树的最大最小是则都是invalid的
    left = helper(root.left)
    right = helper(root.right)
    if root.val > left[0] and root.val < right[1]: # 和当前节点有关
        return [max(root.val, right[0]), min(root.val, left[1]), 1 + left[2] + right[2]]
    return [MAX_VALUE, MIN_VALUE, max(left[2], right[2])]

def largestBSTSubtree(root):
    return helper(root)[2]
''' second Solution '''
class SubTree(object):
    def __init__(self, largest, n, min, max):
        self.largest = largest  # largest BST
        self.n = n              # number of nodes in this ST
        self.min = min          # min val in this ST
        self.max = max          # max val in this ST

class Solution(object):
    def largestBSTSubtree(self, root):
        res = self.dfs(root)
        return res.largest

    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val > left.max and root.val < right.min:  # valid BST
            n = left.n + right.n + 1
        else:
            n = float('-inf')

        largest = max(left.largest, right.largest, n)
        return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))
