'''给定一个整型数组arr，代表数值不同的纸牌排成一条线，玩家A和玩家B依次拿走每张纸牌，
规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左和最右的纸牌，玩家A和玩家B绝顶聪明。
请返回最后的获胜者的分数。
'''
# 先手函数
def f(i,j):
    if i == j: # 如果只剩下一张牌，直接拿走
        return arr[i]
    # 至少两张牌，返回拿左边的然后在剩下里面调用后手函数，同理拿右边的
            #拿左边的
    return max(arr[i] + s(i+1,j),\
     arr[j]+s(i,j-1)) # 拿右边的

#后手函数
def s(i,j):
    if i == j:
        return 0

    # 后手的得分由先手决定，先手的人必然在两种情况下给你最差的所以用min
    return min(f(i+1,j), f(i,j-1))



''' 改动态规划 '''
'''
可变参数是i，j，变换范围是0 到 N-1
两个函数两张二维表，因为有两个可变参数
我们需要的是两张表的右上角 f[0][N-1] s[0][N-1]
base case
f 表的对角线是由arr确定
s 表的对角线都是0
任意位置 f 表的数值右s表中对应位置的下边和左边决定 f(i+1,j), f(i,j-1)
s表同理
所以沿着对角线，往右上角靠近
'''
def windp(arr):
    N = len(arr)
    f = [[0 for _ in range(N)] for _ in range(N)]
    s = [[0 for _ in range(N)] for _ in range(N)]

    # 补充f的对角线
    for i in range(N):
        f[i][i] = arr[i]
    # 0,0 右下方移动已经填好
    # 0,1
    # 0,2
    # 0, N-1
    for col in range(1,N):
        # 对角线的出发位置 0，col
        L = 0
        R = col
        while L < N and R < N:
            # 填写过程和递归函数保持一致
            f[L][R] = max(arr[L] + s[L+1][R], arr[R] + s[L][R-1])
            s[L][R] = min(f[L+1][R], f[L][R-1])
            # 右下角移动，两边都加一
            L += 1
            R += 1
    return max(f[0][N-1], s[0][N-1])

arr = [1,2,100,4]
# 返回先拿还是后拿中最大的
print(max(f(0,3),s(0,3)))
print(windp(arr))
