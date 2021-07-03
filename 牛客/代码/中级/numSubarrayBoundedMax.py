class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, dp, prev = 0, 0, -1
        for i, n in enumerate(nums):
            if n > right:
                dp = 0
                prev = i
            elif n >= left:
                dp = i - prev
            res += dp
        return res
