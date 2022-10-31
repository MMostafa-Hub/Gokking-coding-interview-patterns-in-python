"""
Leetcode: https://leetcode.com/problems/sliding-window-maximum/

Given an integer array and a window of size w, find the current maximum value in the window as it slides through the entire array.

Note:
    If the window size is greater than the array size, we consider the entire array as a single window.

Constraints:
    1 <= array.length < 1e3
    -10 <= array[i] <= 1e4
    1 <= w
"""

from collections import deque
from typing import List


def find_max_sliding_window(nums: List[int], window_size: int) -> List[int]:
    if not nums: return []
    if window_size > len(nums): window_size = len(nums)
    
    res = []

    # storing only the max element index in the first window
    window = deque()
    for i in range(window_size):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)
    print(window)   
    res.append(nums[window[0]])
      
    for i, num in enumerate(nums[window_size:], start=window_size):
        while window and num >= nums[window[-1]]:
            window.pop()
            
        # pops the elements that are not in the window
        while window and not (i - window_size + 1 <= window[0] <= i ):
            window.popleft()
        
        window.append(i)
        res.append(nums[window[0]])
        
    return res

