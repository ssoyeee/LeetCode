class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # closed: open mapping
        bracket = {')':'(',
                    '}':'{',
                    ']':'['}
        for char in s:
            if char in bracket: # if closed bracket
                if not stack or stack[-1] != bracket[char]:
                    # stack empty or top doesn't match expected open bracket
                    return False
                stack.pop() # matched, pop from stack
            else: # if opened bracket
                stack.append(char) # push to stack
        # True if all brackets matched, False if unclosed remain        
        return not stack

        
        # T: O(N) -- iterate through string once
        # S: O(N) -- stack stores open brackets