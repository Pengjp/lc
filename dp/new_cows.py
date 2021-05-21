'''假设农场中成熟的母牛每年只会生 1 头小母牛，并且永远不会死。第一年农场中有一只成熟的母牛，
从第二年开始，母牛开始生小母牛。每只小母牛 3 年之后成熟又可以生小母牛。给定整数 n，求出 n 年后牛的数量。
'''
def recursive(n):
    if n <= 4:
        return n
    return recursive(n-1) + recursive(n-3)
def dp(n):
    if n <= 4:
        return n
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    if n <= 4 and n > 1:
        for i in range(2,n+1):
            dp[i] = dp[i-1] + 1
    if n > 4:
        for i in range(2,5):
            dp[i] = dp[i-1] + 1
        for i in range(5,n+1):
            dp[i] = dp[i-1] + dp[i-3]
    return dp[-1]
def dp1(n):
    if n <= 4:
        return n
    dp = [i for i in range(1,5)]
    from collections import deque
    dp = deque(dp)
    ans = 0
    i = 5
    while i <= n:
        ans = dp[3] + dp[1]
        dp.popleft()
        dp.append(ans)
        i += 1
    return ans % (1e9 + 7)

n = 6
print(recursive(n))
print(dp(n))
print(dp1(n))
