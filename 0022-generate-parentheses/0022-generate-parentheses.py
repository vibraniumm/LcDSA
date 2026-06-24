class Solution:
    def generateParenthesis(self, n):

        result = []

        def solve(s, open_brackets, close_brackets):

            if len(s) == 2 * n:
                result.append(s)
                return

            if open_brackets < n:
                solve(s + "(", open_brackets + 1, close_brackets)

            if close_brackets < open_brackets:
                solve(s + ")", open_brackets, close_brackets + 1)

        solve("", 0, 0)

        return result