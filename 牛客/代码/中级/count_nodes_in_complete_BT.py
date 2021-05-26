'''
求出完全二叉树的节点个数，小于O(N)
利用递归
1. 求出树的深度，一直沿着左节点走
2. 看右树的左边界深度是否到最大深度
    如果存在，则证明左树是满的高度为整棵树的高度
    不存在，则右数是满的，但是高度是最大高度减一
   之后利用递归求另外一个数的高度
'''
def height(node, level):
    while node:
        level += 1
        node = node.left
    return level - 1
    
def bs(node, level, h):
    '''
    node -> current node
    level -> current node level
    h -> deepest level, a fixed parameter
    '''
    if level == h: # leaf node
        return 1
    # 传入右树，右数会在level + 1 层 求出右树上最大深度
    # 如果右树的最大深度到了全局的最大深度，则证明左数是完整的，只需要
    # 计算右数右多少节点
    if height(node.right, level+1) == h:
        return 2**(h-level) + bs(node.right, level+1, h)
    else: # 此时证明右树是满的，右树高度是少一层
        return 2**(h-level-1) + bs(node.left, level+1, h)
