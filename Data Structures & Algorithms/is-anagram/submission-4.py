class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_catalog = {}

        for char in s:
            if s_catalog.get(char) != None:
                s_catalog[char] += 1
            else:
                s_catalog[char] = 1

        for char in t:
            if s_catalog.get(char) == None:
                return False
            else:
                s_catalog[char] -= 1
                if s_catalog[char] == 0:
                    s_catalog.pop(char)
        
        return True