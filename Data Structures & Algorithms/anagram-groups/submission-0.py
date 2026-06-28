class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            sortedS = ''.join(sorted(word))
            d[sortedS].append(word)

        return list(d.values())



