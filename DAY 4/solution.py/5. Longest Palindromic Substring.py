class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        start = 0
        end = 0

        for i in range(len(s)):

            left, right = self.expand(s, i, i)
            left2, right2 = self.expand(s, i, i + 1)

            if right - left > end - start:
                start = left
                end = right

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]

    def expand(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:

            left -= 1
            right += 1

        return left + 1, right - 1