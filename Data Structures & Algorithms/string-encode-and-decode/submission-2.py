class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []

        
        for word in strs:
            i = str(len(word)) + "#"
            i += word

            enc.append(i)
        
        encStr = "".join(enc)

        return encStr

    def decode(self, s: str) -> List[str]:
        
        ans = []
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1

            lengthWord = int(s[i:j])

            i = j + 1
            j = i + lengthWord
            ans.append(s[i:j])
            i = j

        return ans