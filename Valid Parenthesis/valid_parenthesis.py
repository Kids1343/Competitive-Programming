class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = "({["
        for c in s:
            if c in openings:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == ")" and stack.pop() != "(":
                return False
            elif c == "]" and stack.pop() != "[":
                return False
            elif c == "}" and stack.pop() != "{":
                return False

        return len(stack) == 0
