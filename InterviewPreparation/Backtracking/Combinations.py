'''Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
'''

def combine(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:  # Base case: combination of size k
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)  # Choose a number
            backtrack(i + 1, path)  # Recurse with next number
            path.pop()  # Backtrack (remove last added number)

    backtrack(1, [])
    return result