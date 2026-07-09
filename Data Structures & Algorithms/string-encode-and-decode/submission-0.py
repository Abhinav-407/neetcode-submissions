class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = len(string)
            result += str(length) + '#'+ string
        return result

    def decode(self, s: str) -> List[str]:
        
        strs = []
        i=0
        while i < len(s):
            length = ""
            string = ""
            while s[i] != '#':
                length += s[i]
                i+=1
            string += s[i+1:i+1+int(length)]
            i = i+1+int(length)
            strs.append(string)
        return strs
