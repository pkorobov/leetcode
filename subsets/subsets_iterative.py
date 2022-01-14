class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for elem in nums:
            result += [s + [elem] for s in result]
        return result
