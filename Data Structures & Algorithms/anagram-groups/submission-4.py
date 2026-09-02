class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs: 
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] +=1 

            res[tuple(count)].append(word) #bc lists cant be keys

        return list(res.values()) 