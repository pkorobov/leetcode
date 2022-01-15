class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = nums[:3]
        for i in range(2, len(nums)):
            dp[i % len(dp)] = max(dp[(i - 1) % len(dp)], nums[i] + dp[(i - 2) % len(dp)])
        return max(dp[(len(nums) - 1) % len(dp)], dp[(len(nums) - 2) % len(dp)])
