class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                r = stack.pop()
                l = stack.pop()
                result = int(eval("("+l+")"+i+"("+r+")"))
                stack.append(str(result))
        return int(stack[0])
            

        