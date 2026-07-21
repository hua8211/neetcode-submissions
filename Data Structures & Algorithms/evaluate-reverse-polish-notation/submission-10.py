class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        math = ["+", "-", "*", "/"]
        for c in tokens:
            print(c)
            if c in math:
                temp2 = int(stack.pop())
                temp1 = int(stack.pop())
                if c == "+":
                    stack.append(temp1 + temp2)
                if c == "-":
                    stack.append(temp1 - temp2)
                if c == "*":
                    stack.append(temp1 * temp2)
                if c == "/":
                    if temp2 == 0 :
                        stack = [0]
                    else:
                        stack.append(int(temp1 / temp2))
            else:
                stack.append(int(c))
            print(stack)
        return stack.pop()