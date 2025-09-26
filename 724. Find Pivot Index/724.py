# https://leetcode.com/problems/find-pivot-index

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for i, x in enumerate(nums):
            right -= x
            if left == right:
                return i
            left += x

        return -1


# Input
# nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
nums = [2, 1, -1]

# Output
solution = Solution()
indices = solution.pivotIndex(nums)
print(indices)
