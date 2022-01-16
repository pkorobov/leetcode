class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []

        l_prev, r_prev = intervals[0]
        for i in range(1, len(intervals)):
            l_cur, r_cur = intervals[i]
            if r_prev >= l_cur and r_cur > r_prev:
                r_prev = r_cur
            elif r_prev < l_cur:
                result.append([l_prev, r_prev])
                l_prev, r_prev = intervals[i]
            i += 1
        result.append([l_prev, r_prev])
        return result
