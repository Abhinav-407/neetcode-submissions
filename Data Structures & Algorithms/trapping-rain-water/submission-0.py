class Solution:
    def trap(self, height: List[int]) -> int: 
        n = len(height)
        left = 0
        right = n - 1

        left_max = height[left]
        right_max = height[right]

        water = 0

        while left < right:

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water