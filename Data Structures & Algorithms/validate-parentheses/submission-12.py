class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                if (stack[-1] == '(' and char != ')' or
                stack[-1] == '{' and char != '}' or
                stack[-1] == '[' and char != ']'):
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0