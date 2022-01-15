class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # any permutation is a composition of transpositions
        # [1, 2, 3, 4] -> [2, 1, 3, 4] or [3, 2, 1, 4] or [4, 2, 3, 1]
        # then reduce task to nums[1:n] and etc.
        self.result = []
        self._permute(nums, 0)
        return self.result

    def _permute(self, nums: List[int], start: int):
        if start == len(nums) - 1:
            self.result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            self._permute(nums, start + 1)
            nums[i], nums[start] = nums[start], nums[i]
