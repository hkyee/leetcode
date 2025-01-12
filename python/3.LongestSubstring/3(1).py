# Find the longest substring without repeating character

# Example 
# Input: a b c a b c d b b
# Output: 4 (a b c d)


A = input("Enter a list of characters separated with spaces \n").split()
A = list(A)



def longestSubString(chars):
    
    char_dic = {}
    maxLength = 0
    start = 0               # This variable is used to minus off the previous repeated character

    for i in range(len(chars)):
        if chars[i] in char_dic:
            start = char_dic[chars[i]] + 1
        else:
            maxLength = max(maxLength , i-start+1)
        char_dic[chars[i]] = i
        
    return maxLength


print(longestSubString(A))



