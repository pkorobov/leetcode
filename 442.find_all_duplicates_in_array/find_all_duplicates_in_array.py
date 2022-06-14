class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = list()
        for elem in nums:
            key = abs(elem) - 1
            if nums[key] > 0:
                nums[key] *= -1
            else:
                result.append(abs(elem))
        return result