# https://leetcode.com/problems/two-sum/ #

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i, num in enumerate(nums):
            if target - num in numToIndex:
                return numToIndex[target - num], i
            numToIndex[num] = i


# Input
nums = [2, 7, 11, 15]
target = 9

# Output
solution = Solution()
indices = solution.twoSum(nums, target)
print(indices)
