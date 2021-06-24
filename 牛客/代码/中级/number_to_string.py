def process(arr, index):
    # 如果来到最后一个位置，则前面的路径都考虑完
    if index == len(arr):
        return 1
    if arr[index] == '0':
        return 0
    res = process(arr,index+1)
    if index == len(arr) - 1:
        return res
    if int(arr[index]) * 10 + int(arr[index+1]) < 27:
        res += process(arr, index+2)
    return res

# 递归变dp
def dpway(arr):
    N = len(arr)
    dp = [0 for _ in range(N+1)]
    dp[N] = 1
    dp[N-1] = 0 if int(arr[N-1]) == 0 else 1
    for i in range(N-2, -1, -1):
        if int(arr[i]) == 0:
            dp[i] = 0
        else:
            # f(i) = f(i+1) + 如果i和i+1一起不大于27的话 f(i+2)
            i_2 = dp[i+2] if int(arr[i]) * 10 + int(arr[i+1]) < 27 else 0
            dp[i] = dp[i+1] + i_2
    return dp[0]

def dpway2(arr):
    n = len(arr)
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 0 if int(arr[0]) == 0 else 1 # 如果第一个字符不是0，则答案为1
    for i in range(2,n+1):
        one = int(arr[i-1])
        two = int(arr[i-2]) * 10 + int(arr[i-1])
        print(i, one, two)
        if one >= 1 and one <= 9:
            dp[i] += dp[i-1]
        if two < 27 and two >= 10:
            dp[i] += dp[i-2]
        print(dp)
    return dp[n]

# print(dpway('226'))
print(dpway2('226'))
