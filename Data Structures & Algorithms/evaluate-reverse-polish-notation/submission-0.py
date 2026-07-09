class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+","-","/","*"}:
                stack.append(int(token))
            else:
                if token == "+":
                    a = stack.pop()
                    b = stack.pop()
                    result = a+b
                    stack.append(result)
                if token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    result = b-a
                    stack.append(result)
                if token == "*":
                    a = stack.pop()
                    b = stack.pop()
                    result = a*b
                    stack.append(result)
                if token == "/":
                    a = stack.pop()
                    b = stack.pop()
                    result = int(b/a)
                    stack.append(result)
        return stack[-1]