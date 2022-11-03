"""
Lintcode: https://www.lintcode.com/problem/857/
Leetcode (premium): https://leetcode.com/problems/minimum-window-subsequence/

Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1,
such that every character of str2 appears in sub_str in the *same order* as it is present in str2.

Note:
    - If there is no window in str1 that covers all characters in str2, return an empty string.
    - If there are multiple minimum-length windows, return the one with the leftmost starting index.

Constraints:
    1 <= str1.length <= 2e3
    1 <= sr2.length <= 100
    str1 and str2 consist of uppercase and lowercase English letters.

"""
import math


def min_window(s1: str, s2: str) -> str:
    start, end = 0, 0
    min_sub_sequence = ""
    min_length = math.inf
    """
                         i 
        s1 = a, b, c, d, e, b, d, d, e
                     j
        s2 = b, d, e
    
    """
    s2_i, s1_i = 0, 0
    while s1_i < len(s1):
        # increment s2_i as s2[s2_i] == s1[s1_i] 
        if s2[s2_i] == s1[s1_i]: 
            s2_i += 1
            
            # until s2_i reaches its end, we have a substring s1[:s1_i] that contains s2
            if s2_i == len(s2):
                s2_i -= 1
                start, end = s1_i, s1_i + 1
                
                # now we try do decrease the size of substring 
                while s2_i >= 0:
                    if s1[start] == s2[s2_i]:
                        s2_i -= 1
                    
                    start -= 1

                # update min_length and min_sub_sequence
                if end - start < min_length:
                    min_sub_sequence = s1[start + 1:end]
                    min_length = end - start
                
                # initialize s2_i 
                s2_i = 0
                # start searching for a new sequence after start pointer
                s1_i = start + 1
        s1_i += 1
    return min_sub_sequence

# Driver code
def main():
    str1 = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa",
            "qwewerrty", "aaabbcbq", "zxcvnhss", "alpha",
            "beta", "asd", "abcd"]
    str2 = ["bde", "kzed", "werty", "abc", "css", "la", "ab", "as", "pp", "quitwlnicl"]
    for i in range(len(str1)):
        print(i+1, ". \tInput string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\tSubsequence string: ", min_window(str1[i], str2[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
