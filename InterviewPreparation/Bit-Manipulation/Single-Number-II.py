'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''

def singleNumber(nums: list[int]) -> int:
    result = 0
    
    # Iterate through each bit position (32 bits for a signed integer)
    for i in range(32):
        bit_count = 0
        
        # Count how many numbers have the i-th bit set
        for num in nums:
            if (num >> i) & 1:
                bit_count += 1
        
        # If bit_count is not a multiple of 3, set this bit in the result
        if bit_count % 3 != 0:
            result |= (1 << i)
    
    # Handle negative numbers (since Python uses unlimited bit-length integers)
    if result >= 2**31:
        result -= 2**32
    
    return result
