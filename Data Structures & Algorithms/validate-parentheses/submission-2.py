class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or pairs[i] != stack.pop():
                    return False
        if not stack:
            return True
        return False