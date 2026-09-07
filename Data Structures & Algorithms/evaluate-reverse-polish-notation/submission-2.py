def perform(num1, num2, op):
   match op:
    case "+":
        return num1+num2
    case "-":
        return num1-num2
    case "/":
        return int(num1/num2)
    case "*":
        return num1*num2

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for char in tokens:
            if char not in operators:
                stack.append(int(char)) 
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                val = perform(num1, num2, char)
                stack.append(val)
        return stack[-1]