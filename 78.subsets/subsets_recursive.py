class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = self.dfs(nums)
        return result

    def dfs(self, current_set: List[int]):
        if len(current_set) == 0:
            return [[]]
        next_sets = self.dfs(current_set[1:])
        return next_sets + [s + [current_set[0]] for s in next_sets]
