'''Given an integer array nums, return the length of the longest strictly increasing 
subsequence

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1'''

import bisect

def lengthOfLIS(nums):
    sub = []
    
    for num in nums:
        i = bisect.bisect_left(sub, num)  # Find index to replace
        if i < len(sub):
            sub[i] = num  # Replace element
        else:
            sub.append(num)  # Extend sequence

    return len(sub)
