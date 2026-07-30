class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = defaultdict(int) 
        #using default dict so that we can immediate increment count / defaults count of key value to 0
        tFreq = defaultdict(int)

        for char in s:
            sFreq[char] += 1
        
        for char in t:
            tFreq[char] += 1

        return sFreq == tFreq


        