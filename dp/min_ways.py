'''
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，
路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
'''
def dp(arr):
    n = len(arr)
    m = len(arr[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = arr[0][0]
    # 补充上边界
    for i in range(1,m):
        dp[0][i] = dp[0][i-1] + arr[0][i]
    # 补充左边界
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + arr[i][0]
    for row in range(1,n):
        for col in range(1,m):
            dp[row][col] = arr[row][col] + min(dp[row-1][col],dp[row][col-1])
    return dp[-1][-1]

def shortestRoadSum(arr):
    n = len(arr)
    m = len(arr[0])
    dp = arr[0]
    # 更新第一行的结果
    for j in range(1, m):
        # 第一行只能由左向右走
        dp[j] += dp[j - 1]
    # print(dp)
    for i in range(1, n):
        dp[0] += arr[i][0] #每一行开始遍历时更新第一个元素
        for j in range(1, m):
            dp[j] = min(dp[j-1],dp[j]) + arr[i][j]
        print(dp)
    return dp[-1]

arr = [[1,3,5,9],\
       [8,1,3,4],\
       [5,0,6,1],\
       [8,8,4,0]]
print(dp(arr))
print(shortestRoadSum(arr))
