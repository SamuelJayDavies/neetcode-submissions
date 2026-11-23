class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in ["(", '{', "["]:
                stack.append(c)
            elif c in [")", "}", "]"]:
                if not stack or pairs.get(stack.pop()) != c:
                    return False
        
        return not stack