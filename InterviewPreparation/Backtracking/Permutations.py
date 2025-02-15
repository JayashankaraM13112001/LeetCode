'''Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]'''

def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):  # Base case: permutation complete
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:  # Check if number is already used
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)  # Recurse for next position
                path.pop()  # Backtrack (remove last added number)
                used[i] = False

    backtrack([], [False] * len(nums))
    return result