class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = []
        for s in strs:

            encoded_str.append(s)
            encoded_str.append("¬")
        
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '¬':
                j += 1

            res.append(s[i:j])
            i = j+1
        
        return res

        