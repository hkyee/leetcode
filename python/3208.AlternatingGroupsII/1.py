class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        # Left Pointer
        l = 0
        res = 0
        # Right pointer
        # We add k - 1 because of circular array
        for r in range(1, N + k - 1):
            # We only update left pointer when right - 1 and right are the same
            # This is because we only want alternating
            # The only options are 1 and 0
            # SLiding Window
            # Because they are the same, they will NEVER be alternating elements
            if colors[r % N] == colors[(r - 1) % N]:
                l = r
            # Ensures r and l gap are within k
            if r - l + 1 > k:
                l += 1

            if r - l + 1 == k:
                res += 1
        return res


# Time : O(n)
# Space : O(1)
# https://www.youtube.com/watch?v=Zexx16dNPX8
