class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -999999
        cur = 0
        for i in nums:
            cur += i
            ans = max(ans, cur)
            cur = max(0, cur)
        return ans
