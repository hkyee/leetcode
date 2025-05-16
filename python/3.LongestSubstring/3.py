class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left = left + 1

                charSet.add(s[right])
        return maxLength


# right and left are pointers
# if a character is not in Charset, we add it

# if it is, then we remove the Charset from the begining until the reappearing character, and we add the reappeared character into Charset.

# Example:

# s = "abcabcbb"
# Charset = a -> ab -> abc -> bca ..

# s = "pwwkew"
# Charset = p -> pw -> w ..
