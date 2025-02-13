'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]'''

def search_range(nums, target):
    def find_first(nums, target):
        low, high = 0, len(nums) - 1
        first = -1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid  # Potential first occurrence
                high = mid - 1  # Move left to check earlier occurrences
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def find_last(nums, target):
        low, high = 0, len(nums) - 1
        last = -1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid  # Potential last occurrence
                low = mid + 1  # Move right to check later occurrences
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    first = find_first(nums, target)
    last = find_last(nums, target)
    return [first, last]