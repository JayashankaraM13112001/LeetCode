'''Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23'''


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        result = 0
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ["+", "-"]:
                result += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        
        return result + sign * num