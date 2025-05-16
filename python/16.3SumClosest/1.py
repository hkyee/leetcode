class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the input list to use two-pointer technique
        nums.sort()

        # Initialize the result with the sum of the first three elements
        result = nums[0] + nums[1] + nums[2]

        # Loop through the array, fixing one element at a time
        for i in range(len(nums) - 2):
            # Initialize two pointers: one just after i, one at the end
            j, k = i + 1, len(nums) - 1

            # While the two pointers haven't met
            while j < k:
                # Calculate the current sum of the triplet
                sum = nums[i] + nums[j] + nums[k]

                # If the exact target sum is found, return it immediately
                if sum == target:
                    return sum

                # Update the result if the current sum is closer to the target
                if abs(sum - target) < abs(result - target):
                    result = sum

                # Move pointers based on comparison to target
                if sum < target:
                    j += 1  # Increase the sum by moving left pointer right
                elif sum > target:
                    k -= 1  # Decrease the sum by moving right pointer left

        # Return the closest sum found after checking all possibilities
        return result
