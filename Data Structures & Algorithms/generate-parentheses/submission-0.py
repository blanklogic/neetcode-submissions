class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op, cl = 0, 0
        stack = []
        res = []

        def backtrack(op, cl):
            if op == cl == n:
                res.append("".join(stack))
            if op < n:
                stack.append("(")
                backtrack(op + 1, cl)
                stack.pop()
            if op > cl:
                stack.append(")")
                backtrack(op, cl + 1)
                stack.pop()
        backtrack(0, 0)
        return res
