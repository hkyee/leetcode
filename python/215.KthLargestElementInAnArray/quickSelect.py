class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        Left = [x for x in nums if x > pivot]
        Right = [x for x in nums if x < pivot]
        Mid = [x for x in nums if x == pivot]

        L = len(Left)
        M = len(Mid)

        if k <= L:
            return self.findKthLargest(Left, k)
        elif k > L + M:
            return self.findKthLargest(Right, k - L - M)
        else:
            return Mid[0]
