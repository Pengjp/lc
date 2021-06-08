''' 最长无重复子序列 '''
'''' Longest Substring Without Repeating Characters '''
def lengthOfLongestSubstring(arr):
    start, ans = 0, 0
    seen = {}
    for index, ele in enumerate(arr):
        # 如果当前位置见到过，并且子序列的开始的位置是小于等于这个已经见过的元素的位置，更新
        if ele in seen and start <= seen[ele]:
            start = seen[ele] + 1
        else:
            ans = max(ans, index - start + 1)
        seen[ele] = index
    return ans

print(lengthOfLongestSubstring([2,2,3,4,5]))
print(lengthOfLongestSubstring([2,1,3,3,4,5,6,7]))
