# Given a string s, find the length of the longest substring without duplicate characters.

def lengthOfLongestSubstring(s):
    seen = set()
    l = 0
    longest = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        
        seen.add(s[r])
        w = r - l + 1
        longest = max(longest, w)
    return longest

s = "abcabcbb"
print(lengthOfLongestSubstring(s))