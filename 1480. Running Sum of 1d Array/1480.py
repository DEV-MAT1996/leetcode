# https://leetcode.com/problems/running-sum-of-1d-array

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        sum_arr = []

        for i in nums:
            sum += i
            sum_arr.append(sum)

        return sum_arr


# Input
nums = [1, 2, 3, 4]

# Output
solution = Solution()
indices = solution.runningSum(nums)
print(indices)
