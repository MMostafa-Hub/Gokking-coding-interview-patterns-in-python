"""
leetcode link: https://leetcode.com/problems/circular-array-loop/

An input array containing non-zero integers is given,
where the value at each index represents the number of places to skip forward (if the value is positive)
or backward (if the value is negative).
When skipping forward or backward,wrap around if you reach either end of the array.
For this reason, we are calling it a circular array.
Determine if this circular array has a cycle. 
A cycle is a sequence of indices in the circular array characterized by the following:

Constraints:
    - 1 <= nums.length <= 5000
    - -1000 <= nums[i] <= 1000
    - nums[i] != 0

Test Cases:
    - [2, -1, 1, 2, 2] -> True
    - [3, -3, 2, -2] -> False
    - [1, 4, 3, 2, 1] -> True
    - [5, -1, 1, 1, -7, -9] -> False
    - [2, 5, -4, 3, -1, 4] -> False
"""

from functools import lru_cache
from typing import List

def circular_array_loop(arr: List[int]) -> bool:
    # makes a map of parameters to the result of the function
    # to avoid repeated calculations
    @lru_cache(maxsize=None)
    def next_index(index: int) -> int:
        return (index + arr[index]) % len(arr)

    for i, _ in enumerate(arr):
        fast = slow = i
        # to have a cycle, the direction of the array must be the same
        # arr[fast] * arr[next_index(fast)] > 0 -> same direction (positive or negative) 
        # arr[slow] * arr[next_index(slow)] > 0 -> same direction (positive or negative)
        while arr[fast] * arr[next_index(fast)] > 0 and arr[slow] * arr[next_index(slow)] > 0:
            # advance the fast pointer by 2 steps
            # and the slow pointer by 1 step
            fast = next_index(next_index(fast))
            slow = next_index(slow)
            
            # if a cycle found
            if fast == slow:
                # we need to check if the cycle has more than 1 element
                # by checking if the next index of the fast is the same as the fast
                if fast == next_index(fast):
                    break
                return True
    return False
    
        
    


# run all test cases on circular_array_loop function
print(
    circular_array_loop([2, -1, 1, 2, 2]),
    circular_array_loop([3, -3, 2, -2]),
    circular_array_loop([1, 4, 3, 2, 1]),
    circular_array_loop([5, -1, 1, 1, -7, -9]),
    circular_array_loop([2, 5, -4, 3, -1, 4]),
    sep="\n"
)
                    