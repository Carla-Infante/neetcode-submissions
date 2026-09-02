class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs: 
            count = [0] * 26 #make a count array for each frequency of each letter of alphabet

            for char in word:
                count[ord(char) - ord("a")] +=1 #increment letter in count for each char in the word

            res[tuple(count)].append(word) #bc lists cant be keys. count array is the key 

        return list(res.values()) #make back to list since return type is list