'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.'''


class Solution:
    def trap(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0  # No water can be trapped if there are fewer than 3 bars

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                # Process the left pointer
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                # Process the right pointer
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped
