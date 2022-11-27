"""
Leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, input_string find the longest substring without repeating characters,
and return the length of that longest substring.

constraints:
1 <= input_string.length <= 5 * 10^4
input_string consists of English letters, digits, symbols and spaces.

test case 1:
s = “conceptoftheday”
output = 8

test case 2:
s = “abba”
output = 2

test case 3:
s = “Ihaveatrampoline”
output = 10

"""

from collections import deque


def find_longest_substring(input_string: str) -> int:
    if not input_string:
        return 0
    """
                                                     r 
    s = I, h, a, v, e, a, t, r, a, m, p, o, l, i, n, e
                          l
    win_map = {I: 0, h: 1, a: 8, v: 3, e: 4, t: 6, r: 7, m: 9, p: 10, o: 11, l: 12, i: 13, n: 14, n: 15 }
    longest_length = 10
    """
    l, longest_sub_length = 0, 0
    win_map = {}

    for r, val in enumerate(input_string):
        # if val is already in the window and the index of val is greater than left pointer
        # move the left pointer to the next index of the last occurrence of val
        if val in win_map and l <= win_map[val]:
            l = win_map[val] + 1

        # update the window map with the current index of val
        win_map[val] = r

        # update the longest length
        longest_sub_length = max(r - l + 1, longest_sub_length)

    return longest_sub_length


"""
test this function with the above test cases
"""
print(find_longest_substring("conceptoftheday"))
print(find_longest_substring("abba"))
print(find_longest_substring("Ihaveatrampoline"))
