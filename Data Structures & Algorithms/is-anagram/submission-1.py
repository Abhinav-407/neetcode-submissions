class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        
        for ch in t:
            if ch in freq:
                if freq[ch] == 0:
                    return False
                freq[ch] -= 1
            else:
                return False
        
        for value in freq.values():
            if value != 0:
                return False
        return True