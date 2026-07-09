class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+","-","/","*"}:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    result = a+b
                    stack.append(result)
                elif token == "-":
                    result = b-a
                    stack.append(result)
                elif token == "*":                
                    result = a*b
                    stack.append(result)
                elif token == "/":
                    result = int(b/a)
                    stack.append(result)
        return stack[-1]