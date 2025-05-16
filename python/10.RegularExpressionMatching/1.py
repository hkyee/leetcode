class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i is for last index of s
        # j is for last index of p
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        # Tuple
        key = (i, j)
        # Remove redundancy, because there might be multiple recursive functions with same parameters.
        # Access value in cache
        if key in cache:
            return cache[key]
        # Both s and p have fully traversed, s = p, return True
        if i == -1 and j == -1:
            cache[key] = True
            return True
        # s still have characters left, p has fully traversed
        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]
        # s has fully traversed, but p still has * or *(s)
        if i == -1 and p[j] == "*":
            k = j
            # Move back in pairs (a*)
            while k != -1 and p[k] == "*":
                k -= 2
            # If p has fully traversed, means it is true
            # Eg: (s = sasb, p = a*b*sasb)
            if k == -1:
                cache[key] = True
                return cache[key]
            # Return false if there are still characters in p
            cache[key] = False
            return cache[key]
        # p still has characters left, but s has fully traversed
        if i == -1 and p[j] != "*":
            cache[key] = False
            return cache[key]

        if p[j] == "*":
            # Check for zero occurence
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return cache[key]
            # Match one or more occurences
            if p[j - 1] == s[i] or p[j - 1] == ".":
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]
        # If the char of s and char of p are the same, move both indexes back by 1
        if p[j] == "." or s[i] == p[j]:
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]
