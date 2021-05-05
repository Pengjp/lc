def lengthOfLongestSubstring(arr):
    start, ans = 0, 0
    seen = {}
    for index, ele in enumerate(arr):
        if ele in seen and start <= seen[ele]:
            start = seen[ele] + 1
        else:
            ans = max(ans, index - start + 1)
        seen[ele] = index
    return ans

print(lengthOfLongestSubstring([2,2,3,4,3]))
