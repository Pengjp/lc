-'''
Morris遍历细节
假设来到当前节点cur，开始时cur来到头节点位置
1）如果cur没有左孩子，cur向右移动(cur = cur.right)
2）如果cur有左孩子，找到左子树上最右的节点mostRight：
a.如果mostRight的右指针指向空，让其指向cur，
然后cur向左移动(cur = cur.left)
b.如果mostRight的右指针指向cur，让其指向null，
然后cur向右移动(cur = cur.right)
3）cur为空时遍历停止
'''
def preorder(root):
    # 只打印第一次出现的，如果一个节点有左孩子，则会出现两次
    if not root:
        return
    cur = root
    mostRight = None
    ans = []
    while cur:
        mostRight = cur.left
        # 如果有左孩子
        if mostRight:
            # 找到左子树上的最右节点
            while mostRight.right and mostRight.right != cur:
                mostRight = mostRight.right
            # 跳出while并且右节点为空，根据规则，让右节点指向cur，cur向左移动
            if not mostRight.right: # 第一次访问
                ans.append(cur.val)
                mostRight.right = cur
                cur = cur.left
                continue
            else: # 意味着第二次访问节点
                mostRight.right = None
        else:
            ans.append(cur.val)
        cur = cur.right
    return ans

def inorder(root):
    if not root:
        return
    cur = root
    mostRight = None
    ans = []
    while cur:
        mostRight = cur.left
        if mostRight:
            while mostRight.right and mostRight.right != cur:
                mostRight = mostRight.right
            if not mostRight.right:
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
        ans.append(cur.val)
        cur = cur.right
    return ans
