'''You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.'''


def canJump(nums):
    if not nums:
        return True
    
    pos=nums[0]
    for i in range(1,len(nums)):
        if pos==0:
            return False
        pos-=1
        pos=max(pos,nums[i])
    
    return True

nums=[1,2,1,1,0,1]
print(canJump(nums))