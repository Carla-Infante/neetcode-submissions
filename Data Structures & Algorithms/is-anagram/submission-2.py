class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = defaultdict(int)
        tFreq = defaultdict(int)
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sFreq[s[i]] += 1
            tFreq[t[i]] += 1

        return sFreq == tFreq