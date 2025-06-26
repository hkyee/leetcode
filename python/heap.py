import heapq


def findKthLargest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # Step 1

    for num in nums[k:]:  # Step 2
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]


print(findKthLargest([5, 3, 6, 2, 1], 2))
