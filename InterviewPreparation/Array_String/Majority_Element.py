'''
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
'''

def majorityElement(self, nums: List[int]) -> int:
        element=None
        count=0
        for num in nums:
            if count==0:
                element=num
            count+=(1 if num==element else -1)
        
        return element