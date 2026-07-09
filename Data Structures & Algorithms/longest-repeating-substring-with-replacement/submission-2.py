class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        freq = {}
        max_freq = 0
        res = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            max_freq = max(max_freq, freq[s[right]])
            window = right - left +1
            while window-max_freq > k:
                
                freq[s[left]] -= 1
                left +=1
                window = right-left+1
            
            res = max(res, right-left+1)

        return res