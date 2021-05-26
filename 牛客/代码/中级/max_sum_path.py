# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.data)
# Function to calculate the maximum root-to-leaf sum in a binary tree
def getRootToLeafSum(root):

    # base case: tree is empty
    if root is None:
        return 0

    # calculate the maximum node-to-leaf sum for the left child
    left = getRootToLeafSum(root.left)

    # calculate the maximum node-to-leaf sum for the right child
    right = getRootToLeafSum(root.right)

    # consider the maximum sum child
    return (left if left > right else right) + root.data

def dfs(root):
    stack = [(root, root.data)]
    ans = 0
    while stack:
        cur, val = stack.pop()
        if not cur.left and not cur.right:
            ans = max(ans, val)
        if cur.left:
            stack.append((cur.left, val+cur.left.data))
        if cur.right:
            stack.append((cur.right, val+cur.right.data))
    return ans

if __name__ == '__main__':

    root = None
    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        8   4   5   6
           /   / \   \
         10   7   9   5
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(8)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(10)
    root.right.left.left = Node(7)
    root.right.left.right = Node(9)
    root.right.right.right = Node(5)

    print(getRootToLeafSum(root))
    print(dfs(root))
