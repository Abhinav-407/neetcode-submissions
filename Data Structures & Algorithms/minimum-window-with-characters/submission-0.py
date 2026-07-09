class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        required = len(need)
        formed = 0

        left = 0

        min_len = float("inf")
        start_idx = 0

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            # Requirement for this character just became satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:

                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    start_idx = left

                left_char = s[left]

                window[left_char] -= 1

                # Requirement is no longer satisfied
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start_idx:start_idx + min_len]