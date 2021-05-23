'''给定一个只包含左右括号的序列，求最长的合法子串满足括号能对应匹配。'''
def maxLength(arr):
    n = len(arr)
    # dp 里面存的是以当前index结尾的位置左边最长的完整字符串。
    # 注意： 如果是（ 则为零因为以（ 结尾不完整
    dp = [0 for _ in range(n)]
    ans = 0
    for i in range(1,n):
        # 遇到 ） 后，因为dp表是从左向右填充，当前 ） 的前一个位置上的数值代表着
        # 那个位置最长的完整，所以我们可以跳过那个长度去看完整区间的前一个，如果
        # 完整区间的前一个是 （，则我们至少有2个长度再加上完整区间的长度
        if arr[i] == ')':
            pre = i - dp[i-1] - 1
            if pre >= 0 and arr[pre] == '(':
                dp[i] = dp[i-1] + 2
                if pre > 0: # 如果pre不越界，还需要加上左括号前一个的长度
                    dp[i] += dp[pre-1]
        ans = max(ans, dp[i])
    return ans
print(maxLength(')()(())((()()') == 6)
