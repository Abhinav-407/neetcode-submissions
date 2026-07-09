class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for word in strs:
            can  = "".join(sorted(word))
            if can in data:
                data[can].append(word)
            else:
                data[can] = [word]
            
        return list(data.values())