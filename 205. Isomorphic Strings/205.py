# https://leetcode.com/problems/isomorphic-strings

from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_map = {}
        reverse_map = {}

        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]

            if letter_s in letter_map and letter_map[letter_s] != letter_t:
                return False

            if letter_t in reverse_map and reverse_map[letter_t] != letter_s:
                return False

            letter_map[letter_s] = letter_t
            reverse_map[letter_t] = letter_s

        return True


# Input
# s, t = "egg", "add"
s, t = "foo", "bar"

# Output
solution = Solution()
indices = solution.isIsomorphic(s, t)
print(indices)
