class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses_map = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map.keys():
                if not stack or parentheses_map[char] != stack.pop():
                    return False
            else:
                # Ignore non-parentheses characters
                continue
        
        # Ensure all parentheses are closed
        return not stack
