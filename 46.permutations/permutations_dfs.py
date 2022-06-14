class Solution(object):
    def dfs(self, nums, level, ans, res, used):
        print(ans)
        if level == len(nums):
            res.append(ans)
        for i in range(len(nums)):
            if not used[i]:
                used[i] = 1
                self.dfs(nums, level + 1, ans + [nums[i]], res, used)
                used[i] = 0
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [0] * len(nums)
        res = []
        self.dfs(nums, 0, [], res, used)
        return res
