# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome(s):
    def isPalindrome(s):
        n = len(s)
        i, j = 0, n -1
        while i< j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1 
        return True
    
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return isPalindrome(s[i:j]) or isPalindrome(s[i+1:j+1])
        i += 1
        j -= 1
    return True

s = "abc"
print(validPalindrome(s))


# removed = 0
#         while i < j:
#             if s[i] != s[j] and removed == 0:
#                 removed += 1
#                 sR, sL = s[i+1:j+1], s[i:j]
#                 if sR == sR[::-1]:
#                     i += 1
#                 elif sL == sL[::-1]:
#                     j -= 1
#                 continue
            
#             if s[i] != s[j] and removed == 1:
#                 return False

#             i += 1
#             j -= 1
        
#         return True
        
