"""
Given an array of numbers, find all unique triplets in the array which gives the sum of zero
"""

A = map(int, input("Enter a list of numbers separated with spaces \n").split())
A = list(A)
A.sort()


def threeSum(nums):
    ans = []
    length = len(nums)
    for i in range(length - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = length - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                ans.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while (
                    l < r and nums[r] == nums[r - 1]
                ):  ## Can be removed, but slower code
                    r -= 1  ##
                l += 1
                r -= 1

    return ans


print(threeSum(A))


"""
i is the element in the array, 
l is the element next to i
r is the last element

For every i, l and r slowly converges in the array

"""
