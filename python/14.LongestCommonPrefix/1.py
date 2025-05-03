class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        # Comparing with the second to last
        for words in strs[1:]:
            while pref != words[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""

                # Update common prefix, effectively comparing words with the same length
                pref = pref[0:pref_len]
        
        return pref
    
