"""
leetcode link: https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target,
find the window size of the shortest contiguous subarray whose sum is greater than or equal to the target value.
If no subarray is found, 0 is returned.

constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

test case 1:
nums = [1, 2, 7, 1, 8]
target = 9
output: 2

test case 2:
nums = [1, 2, 3, 4, 5]
target = 11
output: 3

test case 3:
nums = [7, 2, 4, 6, 5, 8]
target = 6
output: 1
"""

from typing import List

def min_sub_array_len(target: int, nums: List[int]) -> int:
    if not nums: return 0
    window_sum = 0
    min_win_size = float("inf")
    
    # Sliding window 👉👉
    l = 0
    for r, val in enumerate(nums):
        window_sum += val
        # if window_sum is greater than or equal to target, shrink the window until it is less than target
        # while shrinking, keep track of the minimum window size
        # and when the window is shrunk to less than target, break out of the loop
        while window_sum >= target and l <= r:
            min_win_size = min(min_win_size, r - l + 1)
            window_sum -= nums[l]
            l += 1
    
    return int(min_win_size) if min_win_size != float("inf") else 0

# test this code with the above test cases
print(min_sub_array_len(9, [1, 2, 7, 1, 8]))
print(min_sub_array_len(11, [1, 2, 3, 4, 5]))
print(min_sub_array_len(6, [7, 2, 4, 6, 5, 8]))