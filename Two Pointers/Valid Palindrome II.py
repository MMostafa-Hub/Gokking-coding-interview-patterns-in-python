"""
leetcode link: https://leetcode.com/problems/valid-palindrome-ii/

Write a function that takes a string as input and
checks whether it can be a valid palindrome by removing at most one character from it.

Constraints:
    - The string will only consist of English letters.
    - 1 <= s.length <= 1e5
    
Test Cases:
    - "aba" -> True
    - "abca" -> True
    - "abc" -> False
    - "RACEACAR" -> True
    - "abbababa" -> True
    - "abcdeca" -> False
    - "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga" -> True
"""
def helper_is_pal(s: str) -> bool:
    return s == s[::-1]

def is_palindrome(s: str) -> bool: 
    l, r = 0, len(s) - 1
    while l < r:
        if s[r] != s[l]:
            return helper_is_pal(s[l + 1:r + 1]) or helper_is_pal(s[l:r])        
        l += 1
        r -= 1
        
    return True

# run all test cases on is_palindrome function
print(
    is_palindrome("aba"),
    is_palindrome("abca"),
    is_palindrome("abc"),
    is_palindrome("RACEACAR"),
    is_palindrome("abbababa"),
    is_palindrome("abcdeca"),
    is_palindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"),
    sep="\n"
)