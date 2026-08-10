class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        have = 0
        needCount = len(need)

        minLength = float("inf")
        answer = ""

        for right in range(len(s)):

            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == needCount:

                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    answer = s[left:right + 1]

                leftChar = s[left]

                window[leftChar] -= 1

                if leftChar in need and window[leftChar] < need[leftChar]:
                    have -= 1

                left += 1

        return answer