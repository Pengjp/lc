class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval:
            print (printval.dataval)
            printval = printval.nextval
list = SLinkedList()
list.headval = Node(-1)
list.AtEnd(2)
list.AtEnd(2)
list.AtEnd(-1)
# list.listprint()



def reverse(node):
    prev = None
    head = node.headval
    while head:
        next = head.nextval
        head.nextval = prev
        prev = head
        head = next
    return prev


# t = reverse(list)
# while t:
#     print(t.dataval)
#     t = t.nextval

def reverse(node):
    prev = None
    head = node
    while head:
        next = head.nextval
        head.nextval = prev
        prev = head
        head = next
    return prev

def isPail(node):
    # we first find the middle point of the linked list which is s
    s = node.headval
    f = node.headval
    while f.nextval and f.nextval.nextval:
        f = f.nextval.nextval
        s = s.nextval
    # s is the middle point, we then reverse the second half of the list
    r = reverse(s)
    l = node.headval
    while l and r:
        if l.dataval != r.dataval:
            print('not')
            return False
        r = r.nextval
        l = l.nextval
    print('yes')
    return True
print('-----回文-----')
isPail(list)

''' 复杂链表的复制 '''
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.rand = None

def CopyList(head):
    if not head:
        return
    cur = head
    next = None
    # copy node and link to every Node
    # 1 -> 2 become 1 -> 1' -> 2
    while cur:
        next = cur.next # remember the original next
        cur.next = Node(cur.dataval)
        cur.next.next = next
        cur = next
    # copy rand pointer for each node
    cur = head
    curCopy = None
    while cur：
        next = cur.next.next # original next
        curCopy = cur.next # copied node
        curCopy.rand = None if not cur.rand else cur.rand.next # assign rand to copied Node, since we know copied node of old node is its next
        cur = next
    res = head.next # starting node for the next list
    cur = head
    while cur:
        next = cur.next.next
        curCopy = cur.next
        cur.next = next
        curCopy.next = next.next if next else None
        cur = next
    return res

''' 链表中是否有环，并且返回第一个入环的节点'''
''' 利用 set() 作为额外空间，里边list，如果在遍历结束前在set里发现有重复的，则
    证明有环 '''
# 不用set来查找第一个入环的节点
# 第一次用快慢节点，如果两节点重合，则证明有环
# 快回到开头，慢指针停留在原地，两个指针都一次走一步，两者下次相遇处则是第一个入环位置
def getLoopNode(head):
    ''' 找到第一个入环点 n1'''
    if not head or not head.next or not head.next.next:
        return
    n1 = head.next
    n2 = head.next.next
    while n1 != n2:
        if not n2.next or not n2.next.next:
            return None
        n2 = n2.next.next
        n1 = n1.next
    n2 = head
    while n1 != n2:
        n1 = n1.next
        n2 = n2.next
    return n1

def NoLoop(head1, head2):
    cur1 = head1
    cur2 = head2
    # we first find which list is longer and compute the difference of length
    n = 0
    while cur1.next:
        n += 1
        cur1 = cur1.next
    while cur2.next:
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2: # if two lists intersect, end points of both lists must be equal
        return None
    cur1 = head1 if n > 0 else head2 # 哪个链表长，则头变为哪个
    cur2 = head2 if cur1 == head1 else head1
    n = abs(n)
    # 让长的链表先走 差值 n 步
    while n != 0:
        n -= 1
        cur1 = cur1.next
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

def bothLoop(head1, loop1, head2, loop2):
    ''' 三种情况，两个链表各自成环，没有交点
        2. 共享环，第一个入环节点是相同的，第一个相交的位置在环外面，该情况类似于无环链表找交点问题
        3. 共享环，入环节点不同，'''
    cur1, cur2 = None, None
    # 如果两个链表的入环位置相同，等同于无环链表相交问题，不必关心环的情况，只需要查看在入环前是否有交点
    if loop1 == loop2:
        cur1 = loop1
        cur2 = loop2
        n = 0 # find difference of length
        while cur1 != loop1:
            n += 1
            cur1 = cur1.next
        while cur2 != loop2:
            n -= 1
            cur2 = cur2.next
        cur1 = head1 if n > 0 else head2 # 长链表头节点
        cur2 = head2 if cur1 == head1 else head1 # 短链表头节点
        n = abs(n)
        for i in range(n):
            cur1 = cur1.next
        while cur1 !=cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        # 区分情况一和三
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2: # 找到了重合点
                return loop1
            cur1 = cur1.next
        return None

def getIntersectNode(head1, head2):
    # first, we want to find if there are any loops in both lists
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)
    # if there are no loops in both lists
    if not loop1 and not loop2:
        return NoLoop(head1,head2)
    if loop1 and loop2:
        return bothLoop(head1, loop1, head2, loop2)
    return None # 一个有环，一个无环，则为空
