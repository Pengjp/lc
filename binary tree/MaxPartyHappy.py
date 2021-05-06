'''
派对的最大快乐值
员工信息的定义如下:
class Employee {
public int happy; // 这名员工可以带来的快乐值
List<Employee> subordinates; // 这名员工有哪些直接下级
}
公司的每个员工都符合 Employee 类的描述。整个公司的人员结构可以看作是一棵标准的、 没有环的
多叉树。树的头节点是公司唯一的老板。除老板之外的每个员工都有唯一的直接上级。 叶节点是没有
任何下属的基层员工(subordinates列表为空)，除基层员工外，每个员工都有一个或多个直接下级。
这个公司现在要办party，你可以决定哪些员工来，哪些员工不来。但是要遵循如下规则。
1.如果某个员工来了，那么这个员工的所有直接下级都不能来
2.派对的整体快乐值是所有到场员工快乐值的累加
3.你的目标是让派对的整体快乐值尽量大
给定一棵多叉树的头节点boss，请返回派对的最大快乐值。

思路：
使用递归套路，对于x的每个下级节点，均有两种信息需要得到，来或者不来的的快乐数值
如果x来，则x的所有下级都不能来，所以在x来的情况下的快乐值是x自己的快乐数值加上所有x下级不来的快乐数值
如果x不来，则x的下级可来可不来，所以取最大值就行
'''
class Node:
    def __init__(self, happy, subs):
        self.happy = happy #int
        self.subs = subs #list

def process(x):
    # 返回一个tuple，第一个是x不来的，第二个是x来的情况
    if len(x.subs) == 0:
        return (0, x.happy)
    come = x.happy
    notcome = 0
    for sub in x.subs:
        info = process(sub)
        come += info[0]
        notcome += max(sub[0], sub[1])
    return (notcome, come)

def maxhappy(head):
    info = process(head)
    return max(info[0], info[1])
