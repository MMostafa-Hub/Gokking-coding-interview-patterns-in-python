"""
leetcode link: https://leetcode.com/problems/valid-palindrome/
Write a function that takes a string s as input and checks whether it’s a palindrome or not.

Note: A phrase, word or sequence is a palindrome that reads the same backwards as forwards.

Constraints:
- The string won’t have any spaces and will only consist of ASCII characters.
- 1 <= s.length <= 2 * 105
"""

def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1 
    while l <= r:
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1
    return True