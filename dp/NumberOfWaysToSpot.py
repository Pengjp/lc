def recursive(N, cur, rest, end):
    ''' N,end 固定参数
        cur：当前来到的位置
        rest: 剩余步数
    '''
    if rest == 0: # 没有剩余步数
        if cur == end:
            return 1
        else:
            return 0
    if cur == 1: # 来到了棋盘的最左边，只能往右走
        return recursive(N, 2, rest-1, end)
    if cur == N: # 只能往左走
        return recursive(N, N-1, rest-1, end)
    return recursive(N, cur-1, rest-1, end) + recursive(N, cur+1, rest-1, end)

''' 然后通过递归改写到dp，base case就是dp表中直接能填写的，递归的逻辑就是dp表的填写顺序 '''

def waysdp(N:int, start:int, K:int,end:int) -> int:
    '''
    N: 棋盘总体大小
    start, end: 开始和结束位置
    K: 可用步数
    '''
    if N < 2 or K < 1 or start < 1 or start > N or end < 1 or end > N:
        return 0
    # dp 表大小是 N+1 * K+1
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    # 第 0 列，也就是剩余步数为0的情况下，除了终点位置，其他都是0，因为没法走过去了
    dp[end][0] = 1 # 已经在终点位置且剩余步数为0
    for col in range(1, K+1):
        dp[1][col] = dp[2][col-1] # 就是rest - 1 列，第二行的数值 第一行依赖左下角
        dp[N][col] = dp[N-1][col-1] # 就是rest - 1 列，倒数第二行的数值 最后一行 依赖左上角
        for row in range(2, N):
            dp[row][col] = dp[row-1][col-1] + dp[row+1][col-1]
    return dp[start][K]

print(waysdp(7,4,9,5))
print(recursive(7,4,9,5))
