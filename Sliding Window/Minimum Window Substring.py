"""
Leetcode: https://leetcode.com/problems/minimum-window-substring/

Given two strings—s and t, find the smallest window substring of t.
The smallest window substring is the shortest sequence of characters in s that includes all of the characters present in t.
The frequency of each character in this sequence should be greater than or equal to the frequency of each character in t.
The order of the characters doesn’t matter here.

Constraints:
    Strings s and t consist of uppercase and lowercase characters.
    t.length <= s.length 
    1 <= t.length 
    t.length <= 1000

testcase 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    
testcase 2:
    Input: s = “cabwefgewcwaefgcf”, t = “cae”
    Output: "cwae"
    
"""


from collections import Counter
import math


def min_window(s: str, t: str) -> str:
    if not t:
        return ""
    t_count = Counter(t)
    window = Counter()

    # We actually can use the counter intersection
    # to check if the window contains all the characters in t
    # by using this condition: window & t_count == t_count, but it's slower

    # required contains the number of characters in t that we still need to match
    required = len(t_count)
    # current contains the number of characters in t that we have matched
    current = 0

    # Sliding window approach: two pointers 👉👉
    l = 0
    min_window_indices = (-1, -1)
    min_window_size = math.inf
    for r, char in enumerate(s):
        window[char] += 1
        # check if char is in t_count and if it is the last occurrence of char in t_count
        if char in t_count and window[char] == t_count[char]:
            current += 1

        # if the window contains all the characters in t
        # we increment l until we remove a character from the window that is also in t
        # at this point we found a new minimum window
        while current == required:
            if r - l + 1 < min_window_size:
                min_window_indices = (l, r)
                min_window_size = r - l + 1

            window[s[l]] -= 1
            # check if char is in t_count and if it is the first occurrence of char in t_count
            if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                current -= 1
            l += 1

    return (
        s[min_window_indices[0] : min_window_indices[1] + 1]
        if min_window_size != math.inf
        else ""
    )
