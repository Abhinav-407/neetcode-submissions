class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        def freq(string):
            count = 0
            freq = {}
            for s in string:
                freq[s] = freq.get(s,0)+1
            return freq
        target = freq(s1)
        window = freq(s2[:len(s1)])
        if target == window:
            return True
        for right in range(len(s1), len(s2)):
            window[s2[right]] = window.get(s2[right],0)+1
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                window.pop(s2[left])
            left += 1
            if window == target:
                return True

        return False

        