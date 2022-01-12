class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # distance between pointers first meeting point and cycle start
        # =
        # distance between path start and cycle start
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
