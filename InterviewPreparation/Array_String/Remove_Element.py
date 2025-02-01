'''
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
'''

def removeElement(self, nums: list[int], val: int) -> int:
        left=0
        right=len(nums)-1

        if val not in nums:
            return len(nums)
        
        while left<right:
            if nums[left]==val:
                while nums[left]==nums[right]:
                    right-=1
                    if left>=right:
                        return left
                nums[left],nums[right]=nums[right],nums[left]

            left+=1

        return left