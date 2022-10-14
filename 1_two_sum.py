from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes_map = {nums[i]: i for i in range(0, len(nums))}
        for i in range(0, len(nums)):
            second_index = indexes_map.get(target - nums[i])
            if second_index and second_index != i:
                return [i, indexes_map[target - nums[i]]]
