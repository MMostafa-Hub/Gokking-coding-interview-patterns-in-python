"""
Leetcode: https://leetcode.com/problems/repeated-dna-sequences/

Given a string s that represents a DNA sequence, and a number k, return all the contiguous sequences (substrings) of length k that occur more than once in the string.
The order of the returned subsequences does not matter. If no repeated subsequence is found, the function should return an empty set.

None: 
    The DNA sequence is composed of a series of nucleotides abbreviated as A, C, G, T.
    For example, ACGAATTCCG is a DNA sequence. When studying DNA, it is useful to identify repeated sequences in it.

Constraints:
    1 <= s.length < 1e4
    s[i] is either A, C, G or T
    
"""
from collections import Counter, deque

# My Approach using Map, while his approach uses Rolling hashing 🤯
def find_repeated_sequences(nucleotides: str, k: int) -> set:
    res = set()
    seq_counter = Counter()
    window = deque(nucleotides[:k])
    
    seq_counter[nucleotides[:k]] = 1
    
    for _, nucleotide in enumerate(nucleotides[k:], start=k):
        window.popleft()
        window.append(nucleotide)
        str_window = "".join(window)
        seq_counter[str_window] += 1
        if seq_counter[str_window] > 1:
            res.add(str_window) 
    
    return res
