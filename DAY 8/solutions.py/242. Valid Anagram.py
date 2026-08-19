class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        map = {}

        for ch in s:

            if ch in map:
                map[ch] = map[ch] + 1
            else:
                map[ch] = 1

        for ch in t:

            if ch not in map:
                return False

            map[ch] = map[ch] - 1

            if map[ch] < 0:
                return False

        return True