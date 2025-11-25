# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
#  it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    n = len(s)

    i , j = 0, n - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
