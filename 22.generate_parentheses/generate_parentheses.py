class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = list()

        def _generateParenthesis(s: List[str], left: int, right: int):
            if len(s) == 2 * n:
                result.append("".join(s))
            if left < n:
                s.append('(')
                _generateParenthesis(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                _generateParenthesis(s, left, right + 1)
                s.pop()

        _generateParenthesis([], 0, 0)
        return result
