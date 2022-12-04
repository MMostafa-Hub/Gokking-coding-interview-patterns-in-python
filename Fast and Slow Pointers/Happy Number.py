"""
leetcode link: https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in 1 are happy.
Return True if n is a happy number, and False if not.

Constraints:
    - 1 <= n <= 2^31 - 1

Test Cases:
    - 23 -> True
    - 2 -> False
    - 28 -> True
    - 4 -> False
    - 1 -> True
"""
from functools import lru_cache

# lru_cache is used to cache the results of sum_digits function
# so that we don't have to recompute the same value again
@lru_cache(maxsize=None)
def sum_digits(n: int) -> int:
    return sum(int(digit) ** 2 for digit in str(n))

def is_happy_number(n: int) -> bool:
    slow = fast = n
    while fast != 1 and sum_digits(fast) != 1:
        slow, fast = sum_digits(slow), sum_digits(sum_digits(fast))
        # cycle detected
        if slow == fast: return False
        
    return True

# run all test cases on is_happy function
print(
    is_happy_number(23),
    is_happy_number(2),
    is_happy_number(28),
    is_happy_number(4),
    is_happy_number(1),
    sep="\n"
)