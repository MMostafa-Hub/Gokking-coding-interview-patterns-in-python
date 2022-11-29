"""
leetcode link: https://leetcode.com/problems/3sum/

Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum equals the target. Return TRUE if three such integers are found in the array.
Otherwise, return FALSE.

constrains:
    - 3 <= nums.length <= 1e3
    - -1e3 <= nums[i] <= 1e3
    - -1e3 <= target <= 1e3

Test Cases:
    - nums = [1, 2, 3], target = 6, return True
    - nums = [1, -1, -1], target = 2, return False
    - nums = [1, 1, -1], target = 2, return False
    - nums = [1, 2, 4, 6, 8, 20], target = 31, return False
"""

from typing import List

def find_sum_of_three(nums: List[int], target: int) -> bool: 
    nums.sort()
    l, r = 0, len(nums) - 1
    for i, val in enumerate(nums):
        l = i + 1
        while l < r:
            three_sum = val + nums[l] + nums[r]
            if three_sum == target:
                return True
            elif three_sum > target:
                r -= 1
            else:
                l += 1
    
    return False

# Test the function with the above test cases
print(find_sum_of_three([1, 2, 3], 6))
print(find_sum_of_three([1, -1, -1], 2))
print(find_sum_of_three([1, 1, -1], 2))
print(find_sum_of_three([1, 2, 4, 6, 8, 20], 31))
