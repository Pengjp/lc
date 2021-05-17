# 得到i j step的数值，如果越界，则返回0
def getValue(dp, row, col, step):
    if row < 0 or row > 9 or col < 0 or col > 8:
        return 0
    return dp[row][col][step]

def waysdp(a, b, s):
    # 三维 i, j, step
    dp = [[[0 for _ in range(s+1)] for _ in range(9)] for _ in range(10)]
    # base case 如果没有剩余步数，在目的地，则为1，否则是0（default value）
    dp[a][b][0] = 1
    for step in range(1, s+1):
        for i in range(10):
            for j in range(9):
                dp[i][j][step] = getValue(dp, i-2, j+1, step-1)+\
                                getValue(dp, i-1, j+2, step-1)+\
                                getValue(dp, i+1, j+2, step-1)+\
                                getValue(dp, i+2, j+1, step-1)+\
                                getValue(dp, i+2, j-1, step-1)+\
                                getValue(dp, i+1, j-2, step-1)+\
                                getValue(dp, i-1, j-2, step-1)+\
                                getValue(dp, i-2, j-1, step-1)
    return dp[0][0][step]
print(waysdp(7,7,10))
