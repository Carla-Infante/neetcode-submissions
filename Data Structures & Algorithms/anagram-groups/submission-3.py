class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs: 
            sortedWord = ''.join(sorted(word)) #sort word by using ''.join(sorted()) bc sorted returns list of char
            
            anagrams[sortedWord].append(word)
        
        return list(anagrams.values())
