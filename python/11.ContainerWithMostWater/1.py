class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        return self.recursive(left, right, height)

    def recursive(self, left, right, height):
        if left >= right:
            return 0
        # Get the current area
        area = min(height[left], height[right]) * (right - left)

        # Case when left pointer is higher than right pointer
        if height[left] > height[right]:
            # Get the max area of recursive call
            return max(area, self.recursive(left, right - 1, height))

        else:
            # Case when right pointer is higher than left pointer or both same height
            return max(area, self.recursive(left + 1, right, height))
