class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x):
            return sum(elem <= x for elem in nums)

        l, r = 0, len(nums) - 1
        while r > l:
            m = l + (r - l) // 2
            y = f(m)
            if y <= m:
                l = m + 1
            else:
                r = m
        return r
