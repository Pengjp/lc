'''
1143. Longest Common Subsequence
'''

'''
每个位置依赖，左边，上边，左上角三个数值
dp[i][j] =
max {
dp[i-1][j-1] 该条件可以省略因为左边和右边在求出的时候，已经考虑了左上角
dp[i-1][j]
dp[i][j-1]
dp[i][j] 当str1[i] == str2[j]
}
'''
def process(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for i, c in enumerate(text1):
        for j, d in enumerate(text2):
            dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]
