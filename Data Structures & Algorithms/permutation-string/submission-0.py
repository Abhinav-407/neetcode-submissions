class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def freq(string):
            count = 0
            freq = {}
            for s in string:
                freq[s] = freq.get(s,0)+1
            return freq
        s1_dict = freq(s1)
        for i in range(len(s2)):
            window = s2[i:i+len(s1)]
            s2_dict = freq(window)
            if s1_dict == s2_dict:
                return True
        return False
        