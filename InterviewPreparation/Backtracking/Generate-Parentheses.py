'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]'''

def generateParenthesis(n):
    res = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:  # Base case: valid combination found
            res.append(current)
            return

        if open_count < n:  # Can add '(' if we haven't used all n
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:  # Can add ')' if it won't be unbalanced
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return res